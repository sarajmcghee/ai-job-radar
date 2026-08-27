"""Strip repeated company boilerplate from job descriptions.

Nearly every posting from one company repeats an "About us" blurb, a benefits
list and an EEO statement. Those blocks name technologies and research topics,
so counting keywords over the raw text mostly measures how many jobs a company
posted, not what it is hiring for. Anthropic's blurb, for example, made
"Multimodal" appear to be a required skill in 560 of 560 postings.

We treat any sentence that shows up in most of a company's postings as
boilerplate and drop it before skill extraction.
"""
import re
from collections import Counter

SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
MIN_JOBS = 4          # below this there is no reliable repetition signal
SHARE_THRESHOLD = 0.5  # in >= half of a company's postings => boilerplate
MIN_LEN = 25           # ignore fragments like "Apply now." either way


def split_sentences(text):
    return [s.strip() for s in SENTENCE_RE.split(text) if len(s.strip()) >= MIN_LEN]


def find_boilerplate(descriptions):
    """Sentences common to at least SHARE_THRESHOLD of these descriptions."""
    if len(descriptions) < MIN_JOBS:
        return set()
    counts = Counter()
    for d in descriptions:
        counts.update(set(split_sentences(d)))  # set(): once per posting
    cutoff = max(2, int(len(descriptions) * SHARE_THRESHOLD))
    return {s for s, n in counts.items() if n >= cutoff}


def strip(description, boiler):
    if not boiler:
        return description
    kept = [s for s in split_sentences(description) if s not in boiler]
    return " ".join(kept)


def clean_company(jobs):
    """Remove shared boilerplate from one company's postings, in place."""
    descs = [j["_desc"] for j in jobs]
    boiler = find_boilerplate(descs)
    if not boiler:
        return 0
    for j in jobs:
        j["_desc"] = strip(j["_desc"], boiler)
    return len(boiler)
