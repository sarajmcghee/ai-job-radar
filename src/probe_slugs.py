"""One-off discovery tool: find which ATS platform each candidate company uses.

Job boards on Greenhouse / Lever / Ashby all expose an unauthenticated JSON
endpoint keyed by a company slug. We can't know a company's slug (or even which
platform it uses) ahead of time, so we probe all three and keep whatever answers
with a non-empty job list. Output feeds config/companies.json.
"""
import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "ai-job-radar/1.0 (+https://github.com/sarajmcghee/ai-job-radar)"

ENDPOINTS = {
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}",
}


def fetch(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def count_jobs(platform, payload):
    """Each platform wraps its postings differently."""
    if platform == "lever":
        return len(payload) if isinstance(payload, list) else 0
    if isinstance(payload, dict):
        return len(payload.get("jobs", []))
    return 0


def probe(candidate):
    """Try every platform for one slug; return the first that has jobs."""
    name, slug = candidate
    for platform, tmpl in ENDPOINTS.items():
        try:
            payload = fetch(tmpl.format(slug=slug))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError,
                json.JSONDecodeError, ConnectionResetError):
            continue
        n = count_jobs(platform, payload)
        if n > 0:
            return {"name": name, "slug": slug, "platform": platform, "job_count": n}
    return None


def main(path):
    with open(path) as f:
        candidates = [tuple(line.split(",")) for line in f.read().split("\n") if line.strip()]
    candidates = [(n.strip(), s.strip()) for n, s in candidates]

    found = []
    with ThreadPoolExecutor(max_workers=24) as pool:
        for result in pool.map(probe, candidates):
            if result:
                found.append(result)
                print(f"  ok  {result['slug']:<28} {result['platform']:<11} {result['job_count']:>4} jobs",
                      file=sys.stderr)

    found.sort(key=lambda c: c["name"].lower())
    print(json.dumps(found, indent=2))
    print(f"\n{len(found)}/{len(candidates)} candidates resolved", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
