"""Turn free-text job descriptions into structured signal.

Three derivations, all keyword-driven so the results stay explainable and the
whole pipeline stays dependency-free:
  - skills:    which technologies the description asks for
  - family:    what kind of role it is, from the title
  - seniority: what level, from the title
Title order matters in the classifiers below: the first pattern to match wins,
so more specific families are listed before the generic ones.
"""
import json
import re
from pathlib import Path

CONFIG = Path(__file__).resolve().parent.parent / "config"

_taxonomy = json.loads((CONFIG / "skills.json").read_text())
CATEGORIES = _taxonomy["categories"]
SKILLS = [
    {"name": s["name"], "cat": s["cat"], "re": re.compile(s["re"], re.I)}
    for s in _taxonomy["skills"]
]
SKILL_CAT = {s["name"]: s["cat"] for s in SKILLS}

# Checked in order; first match wins.
ROLE_FAMILIES = [
    ("research", r"research (?:scientist|engineer|manager|lead)|\bresearcher\b|member of technical staff|scientific staff|fellows? program|\bpostdoc"),
    ("ml-ai", r"\b(?:machine learning|ML|AI|deep learning|applied|research) engineer\b|applied scientist|applied AI|\bAI\b.*\b(?:engineer|scientist|architect|specialist)\b|\bML\b.*\b(?:scientist|architect)\b|perception engineer|model behaou?r"),
    ("data", r"data (?:scientist|engineer|analyst|architect)|analytics engineer|\bBI\b (?:analyst|engineer)|quantitative"),
    ("infra", r"infrastructure|platform engineer|\bSRE\b|site reliability|devops|systems engineer|network engineer|security engineer|hardware engineer|performance engineer|\bAV engineer\b|reliability"),
    ("swe", r"software engineer|\bSDE\b|backend|back[- ]end|frontend|front[- ]end|full[- ]?stack|mobile engineer|\biOS\b|\bandroid\b engineer|web engineer|engineer(?:ing)? manager|developer|\bQA\b|test engineer"),
    ("product", r"product manager|\bPM\b|program manager|\bTPM\b|product designer|\bUX\b|\bUI\b designer|design(?:er)?\b|technical writer|user research"),
    ("gtm", r"sales|account (?:executive|manager)|marketing|recruit|talent|business development|customer success|solutions (?:engineer|architect)|partnerships?|revenue|community|evangelist|strategist|\bBDR\b|\bSDR\b|go[- ]to[- ]market|\bGTM\b"),
    ("ops", r"finance|accounting|legal|counsel|people ops|human resources|\bHR\b|operations|workplace|executive assistant|chief of staff|procurement|\btax\b|payroll|facilities|trust (?:and|&) safety|policy|communications|education lead"),
]


SENIORITY = [
    ("intern", r"\bintern\b|internship|\bco[- ]op\b|new grad|university|\bPhD\b resident|\bfellows? program\b"),
    ("leadership", r"\bdirector\b|\bVP\b|vice president|\bhead of\b|\bchief\b|\bCTO\b|\bCEO\b"),
    ("principal", r"\bprincipal\b|\bdistinguished\b|\bfellow\b(?!s)|\bL[67]\b"),
    # "Lead" alone is usually a functional title ("APAC Tax Lead"), not an
    # engineering level, so require it to attach to a technical noun.
    ("staff", r"\bstaff\b|\bL5\b|tech(?:nical)? lead|lead (?:engineer|scientist|researcher|developer|architect)"),
    ("senior", r"\bsenior\b|\bsr\.?\b|\bexperienced\b"),
    ("entry", r"\bjunior\b|\bjr\.?\b|\bassociate\b|\bentry[- ]level\b|\bI\b$"),
]


ROLE_RES = [(name, re.compile(pat, re.I)) for name, pat in ROLE_FAMILIES]
SEN_RES = [(name, re.compile(pat, re.I)) for name, pat in SENIORITY]


def extract_skills(text):
    """Return sorted skill names mentioned anywhere in the description."""
    if not text:
        return []
    return sorted(s["name"] for s in SKILLS if s["re"].search(text))


def classify_role(title, department=""):
    for name, rx in ROLE_RES:
        if rx.search(title):
            return name
    for name, rx in ROLE_RES:  # fall back to the department label
        if department and rx.search(department):
            return name
    return "other"


def classify_seniority(title):
    for name, rx in SEN_RES:
        if rx.search(title):
            return name
    return "mid"


def enrich(job):
    """Attach derived fields and drop the raw description.

    Dropping `_desc` here is deliberate: descriptions are megabytes per company
    and we commit these records to git every week.
    """
    desc = job.pop("_desc", "")
    job["skills"] = extract_skills(f"{job['title']} {desc}")
    job["family"] = classify_role(job["title"], job.get("department", ""))
    job["seniority"] = classify_seniority(job["title"])
    return job
