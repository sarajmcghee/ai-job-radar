"""Fetch job postings from public ATS APIs and normalize them to one schema.

Greenhouse, Lever and Ashby each expose an unauthenticated JSON board endpoint.
They disagree on field names, on how they represent remote work, and on whether
they give you description text at all, so each gets its own normalizer that
emits the same dict shape.
"""
import gzip
import html
import io
import json
import re
import time
import urllib.error
import urllib.request

UA = "ai-job-radar/1.0 (+https://github.com/sarajmcghee/ai-job-radar)"

BOARD_URLS = {
    # content=true makes Greenhouse include the full description body.
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true",
}

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
# Only explicit location language. "Distributed" was originally in here and
# matched titles like "Distributed Systems Engineer", flagging onsite roles as
# remote. Location words only, and never inferred from a job title's subject.
REMOTE_RE = re.compile(
    r"\bremote\b|work from home|\bWFH\b|\bwork from anywhere\b|\bfully distributed\b", re.I
)
# Bare "Hybrid"/"Onsite" means not remote. A location like "Hybrid or Remote"
# still counts as remote because REMOTE_RE is checked first.
ONSITE_RE = re.compile(r"\bhybrid\b|\bon-?site\b|\bin[- ]office\b", re.I)


def detect_remote(location, title):
    """Best-effort remote flag from free-text location, with title as backup."""
    if location:
        if REMOTE_RE.search(location):
            return True
        if ONSITE_RE.search(location):
            return False
    # Titles rarely carry location, but "Remote Software Engineer" happens.
    return bool(title and REMOTE_RE.search(title))
# Matches "$150,000 - $200,000" and the "$150K – $200K" shorthand Ashby favours.
SALARY_RE = re.compile(
    r"\$\s?(\d{2,3}(?:,\d{3})?)\s?([Kk])?\s?(?:-|–|—|to)\s?\$?\s?(\d{2,3}(?:,\d{3})?)\s?([Kk])?"
)


def fetch_json(url, timeout=45, retries=3):
    """GET with linear backoff. Boards occasionally 5xx or hang under load."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
                return json.loads(raw.decode("utf-8"))
        except Exception as e:  # noqa: BLE001 - any failure is retryable here
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise last


def clean_text(raw):
    """HTML description -> flat text. Descriptions are only used for keyword
    extraction, so structure is irrelevant and we strip it entirely.

    Greenhouse double-escapes its bodies (a literal "&amp;mdash;" in the JSON),
    so a single unescape leaves entities behind and breaks salary ranges that
    use an em dash. Unescaping twice is safe for prose like this.
    """
    if not raw:
        return ""
    text = html.unescape(html.unescape(raw))
    return WS_RE.sub(" ", TAG_RE.sub(" ", text)).strip()


def parse_salary(*texts):
    """Pull a (min, max) USD pair out of whatever text we have.

    Returns None unless the range looks like a plausible annual salary, which
    filters out revenue figures, funding amounts and hourly rates.
    """
    for text in texts:
        if not text:
            continue
        for lo_s, lo_k, hi_s, hi_k in SALARY_RE.findall(text):
            lo = int(lo_s.replace(",", "")) * (1000 if lo_k else 1)
            hi = int(hi_s.replace(",", "")) * (1000 if hi_k else 1)
            if 30_000 <= lo < hi <= 1_500_000:
                return lo, hi
    return None


def _record(company, platform, jid, title, location, url, posted, desc,
            department="", remote=None, salary=None):
    """The single normalized shape every source funnels into."""
    location = location or ""
    if remote is None:
        remote = detect_remote(location, title)
    return {
        "id": f"{platform}:{company['slug']}:{jid}",
        "company": company["name"],
        "platform": platform,
        "title": title.strip(),
        "department": (department or "").strip(),
        "location": location.strip()[:120],
        "remote": bool(remote),
        "url": url,
        "posted_at": (posted or "")[:10],
        "salary": salary or parse_salary(desc),
        "_desc": desc,  # dropped after skill extraction; never persisted
    }


def from_greenhouse(company, payload):
    out = []
    for j in payload.get("jobs", []):
        desc = clean_text(j.get("content"))
        depts = j.get("departments") or []
        out.append(_record(
            company, "greenhouse", j.get("id"), j.get("title", ""),
            (j.get("location") or {}).get("name", ""),
            j.get("absolute_url", ""),
            j.get("first_published") or j.get("updated_at"),
            desc,
            department=depts[0].get("name", "") if depts else "",
        ))
    return out


def from_lever(company, payload):
    out = []
    for j in payload if isinstance(payload, list) else []:
        cats = j.get("categories") or {}
        desc = clean_text(j.get("descriptionPlain") or j.get("description"))
        posted = j.get("createdAt")
        if isinstance(posted, (int, float)):  # Lever uses epoch milliseconds
            posted = time.strftime("%Y-%m-%d", time.gmtime(posted / 1000))
        out.append(_record(
            company, "lever", j.get("id"), j.get("text", ""),
            cats.get("location", ""), j.get("hostedUrl", ""), posted, desc,
            department=cats.get("department") or cats.get("team", ""),
            remote=True if (cats.get("commitment") or "").lower() == "remote" else None,
        ))
    return out


def from_ashby(company, payload):
    out = []
    for j in payload.get("jobs", []):
        desc = clean_text(j.get("descriptionPlain") or j.get("descriptionHtml"))
        comp = j.get("compensation") or {}
        summary = comp.get("scrapeableCompensationSalarySummary") or \
            comp.get("compensationTierSummary") or ""
        # Ashby's isRemote is set true even for Hybrid onsite roles (one board
        # returned 78 Hybrid/San Francisco jobs all marked isRemote=true), so
        # workplaceType is the field to trust when it is present.
        workplace = (j.get("workplaceType") or "").strip().lower()
        if workplace == "remote":
            remote = True
        elif workplace in ("hybrid", "onsite", "on-site"):
            remote = False
        else:
            remote = None  # unset: fall back to the location heuristic
        out.append(_record(
            company, "ashby", j.get("id"), j.get("title", ""),
            j.get("location", ""), j.get("jobUrl", ""), j.get("publishedAt"), desc,
            department=j.get("department") or j.get("team", ""),
            remote=remote,
            salary=parse_salary(summary),
        ))
    return out


NORMALIZERS = {
    "greenhouse": from_greenhouse,
    "lever": from_lever,
    "ashby": from_ashby,
}


def collect_company(company):
    """Fetch and normalize one company's board. Raises on unrecoverable fetch."""
    platform = company["platform"]
    payload = fetch_json(BOARD_URLS[platform].format(slug=company["slug"]))
    return NORMALIZERS[platform](company, payload)
