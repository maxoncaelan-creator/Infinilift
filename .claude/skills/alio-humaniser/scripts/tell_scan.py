#!/usr/bin/env python3
"""Flag surface-level AI tells in marketing copy.

Surface tells are the weakest signal (see references/paper-findings.md), so this
is a prompt to look again, not a verdict. The construction tells in SKILL.md
still need a human-style read.

Usage:
  python3 tell_scan.py draft.txt            # scan a file
  pbpaste | python3 tell_scan.py            # scan text from stdin
  python3 tell_scan.py ads.txt --limit 30   # also flag lines over 30 characters
  python3 tell_scan.py draft.txt --alio     # add Alio! house-style checks
"""
import argparse
import re
import sys

# (pattern, category, suggestion). Patterns are case-insensitive.
STOCK = [
    (r"\bdelv(e|es|ing)\b", "Say what you'll actually look at."),
    (r"\btapestry\b", "Cut it."),
    (r"\belevat(e|es|ing)\b", "Say what improves, by how much."),
    (r"\bunlock(s|ing)?\b", "Say what they get."),
    (r"\bseamless(ly)?\b", "Describe what actually happens."),
    (r"\bleverag(e|es|ing)\b", "Use 'use'."),
    (r"\brobust\b", "Give the number or cut it."),
    (r"\bgame[- ]changer\b", "Give the result instead."),
    (r"\b(cutting|leading|bleeding)[- ]edge\b", "Name the tool or technique."),
    (r"\bstate[- ]of[- ]the[- ]art\b", "Name the tool or technique."),
    (r"\b(world|first)[- ]class\b", "Show the proof instead."),
    (r"\btop[- ]notch\b", "Show the proof instead."),
    (r"\bhassle[- ]free\b", "Say what they don't have to do."),
    (r"\bpeace of mind\b", "Say what they can stop worrying about, specifically."),
    (r"\bone[- ]stop[- ]shop\b", "List the two or three things you actually do."),
    (r"\bnestled\b", "Give the street or landmark."),
    (r"\blook no further\b", "Cut it."),
    (r"\bwe'?ve got you covered\b", "Say what's included."),
    (r"\bpassionate about\b", "Show it with a detail, or cut it."),
    (r"\bdedicated team\b", "Name the people."),
    (r"\bteam of (highly )?(qualified |skilled )?experts\b", "Name the people and their licence or experience."),
    (r"\bvalued (customers|clients|community)\b", "Cut 'valued'."),
    (r"\bwe pride ourselves\b", "Show the thing you're proud of."),
    (r"\btailored (solutions|approach|plans?)\b", "Say what gets adjusted, for whom."),
    (r"\bsolutions\b", "Name the service."),
    (r"\bholistic\b", "Say what's included."),
    (r"\bsynerg(y|ies)\b", "Cut it."),
    (r"\bempower(s|ing)?\b", "Say what they can now do."),
    (r"\bcurated\b", "Say who chose it and why."),
    (r"\bmeticulous(ly)?\b", "Show the care with a detail."),
    (r"\bcomprehensive\b", "List what's covered."),
    (r"\btestament to\b", "Cut it."),
    (r"\bembark\b", "Use 'start'."),
    (r"\bjourney\b", "Say what actually happens."),
    (r"\b(digital )?landscape\b", "Cut it."),
    (r"\bin today'?s\b", "Cut the scene-setting; start with the point."),
    (r"\bfast[- ]paced\b", "Cut it."),
    (r"\bever[- ]evolving\b", "Cut it."),
    (r"\bnext level\b", "Say what the next level is, in numbers."),
    (r"\bsupercharg(e|es|ing)\b", "Say what improves, by how much."),
    (r"\bboost your (online )?presence\b", "Say 'get more calls' or similar."),
    (r"\bonline presence\b", "Say 'website' or 'Google profile'."),
    (r"\brest assured\b", "Give the reason they can relax."),
    (r"\bsay goodbye to\b", "Cut the before/after cliché."),
    (r"\bdon'?t hesitate to\b", "Just give the next step."),
    (r"\bi hope this (email|message) finds you well\b", "Start with why you're writing."),
    (r"\bat the end of the day\b", "Cut it."),
    (r"\bwhether you'?re\b", "Pick the reader you're actually talking to."),
]

EXPLAIN = [  # tell 1: explaining the moral
    (r"(^|[.!?]\s+)(this|which|that) means\b", "Possible explaining-the-moral line. Try deleting it."),
    (r"(^|[.!?]\s+)that'?s why\b", "Possible explaining-the-moral line. Try deleting it."),
    (r"(^|[.!?]\s+)(ultimately|in short|in conclusion|simply put)\b", "Wrap-up line. Try deleting it."),
    (r"\bbecause you deserve\b", "Explaining the moral. Cut it."),
    (r"\byou deserve\b", "Explaining the moral. Usually cuttable."),
]

FEEL = [  # tell 2: stock body feelings and senses
    (r"\bsinking feeling\b", "Stock feeling. Use a real detail or a customer's words."),
    (r"\bbreathe easy\b", "Stock feeling. Say what they no longer have to deal with."),
    (r"\bsigh of relief\b", "Stock feeling."),
    (r"\bknot in your stomach\b", "Stock feeling."),
    (r"\bheart (racing|pounding|sink)", "Stock feeling."),
    (r"\b(aroma|scent|smell) of\b", "Stock sensory scene-setting. Use an observed detail."),
    (r"(^|[.!?]\s+)imagine\b", "'Imagine…' opener. Show the real thing instead."),
]

PATTERN = [
    (r"\bit'?s not (just )?[^.?!,]{1,40}[.,;]\s*it'?s\b", "'It's not X, it's Y.' Say the point once."),
    (r"\bnot just [^.?!]{1,40}\bbut\b", "'Not just X but Y.' Say the point once."),
    (r"\b(the (secret|result|answer|best part|catch))\?", "Colon/question reveal. State it plainly."),
    (r"\bready to [^.?!]{1,40}\?", "Stock closing question. End on a concrete next step."),
]

US_SPELLING = [
    (r"\boptimiz(e|es|ed|ing|ation)\b", "Australian spelling: optimis-"),
    (r"\b(color|colors|colored)\b", "Australian spelling: colour"),
    (r"\borganiz(e|es|ed|ing|ation)\b", "Australian spelling: organis-"),
    (r"\b(center|centers|centered)\b", "Australian spelling: centre"),
    (r"\banalyz(e|es|ed|ing)\b", "Australian spelling: analys-"),
    (r"\b(favorite|favorites)\b", "Australian spelling: favourite"),
    (r"\b(behavior|behaviors)\b", "Australian spelling: behaviour"),
    (r"\bcustomiz(e|es|ed|ing)\b", "Australian spelling: customis-"),
    (r"\brealiz(e|es|ed|ing)\b", "Australian spelling: realis-"),
    (r"\b(inquiry|inquiries)\b", "Alio! uses 'enquiry'."),
]

ALIO = [
    (r"\bGMB\b|\bGoogle My Business\b", "Say 'Google Business Profile'."),
    (r"\bconversions?\b", "Say 'calls and enquiries'."),
    (r"\bleads?\b", "Say 'calls and enquiries' in client-facing copy."),
    (r"\bweb presence\b|\bdigital footprint\b", "Say 'website'."),
    (r"\bguarantee(d|s)?\b", "No guarantees (Alio! principle: honest, always)."),
]

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✨]")
TRIPLE = re.compile(r"\b[\w'-]+(?: [\w'-]+)?, [\w'-]+(?: [\w'-]+)?,? and [\w'-]+", re.I)


def scan(text, limit=None, alio=False):
    groups = [("STOCK", STOCK), ("EXPLAIN", EXPLAIN), ("FEEL", FEEL), ("PATTERN", PATTERN), ("SPELLING", US_SPELLING)]
    if alio:
        groups.append(("ALIO", ALIO))
    flags = []
    for n, line in enumerate(text.splitlines(), 1):
        for cat, rules in groups:
            for pat, tip in rules:
                for m in re.finditer(pat, line, re.I):
                    flags.append((n, cat, m.group(0).strip(" .!?"), tip))
        if "—" in line:
            flags.append((n, "PUNCT", "—", "Em dash. Use a full stop, comma or colon."))
        # Exclamation marks, not counting the one in "Alio!".
        bangs = len(re.findall(r"!", re.sub(r"\bAlio!", "Alio", line)))
        if bangs:
            flags.append((n, "PUNCT", "!" * bangs, "Exclamation mark. Alio! allows one per page."))
        if EMOJI.search(line):
            flags.append((n, "PUNCT", "emoji", "Emoji. Fine in a casual social caption; never as bullets."))
        if n == first_text_line(text) and opens_with_question(line):
            flags.append((n, "PATTERN", line.strip()[:40], "Opens with a rhetorical question. Lead with the fact or offer."))
        if alio and re.search(r"\bAlio\b(?!!)", line) and not re.search(r"alio\.|@alio", line, re.I):
            flags.append((n, "ALIO", "Alio", "Write the name as 'Alio!'."))
        if limit and len(line.strip()) > limit:
            flags.append((n, "LIMIT", f"{len(line.strip())} chars", f"Over the {limit}-character limit."))
    triples = len(TRIPLE.findall(text))
    return flags, triples


def opens_with_question(line):
    # Ignore questions inside quotes, e.g. The answer to "how long?" is...
    unquoted = re.sub(r'"[^"]*"|“[^”]*”', "", line)
    first = re.match(r"\s*[^.!?]*[.!?]", unquoted)
    return bool(first) and first.group(0).endswith("?")


def first_text_line(text):
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip() and not line.lower().startswith("subject:"):
            return n
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="Text file to scan (default: stdin)")
    ap.add_argument("--limit", type=int, help="Flag lines longer than this many characters (e.g. 30 for ad headlines)")
    ap.add_argument("--alio", action="store_true", help="Add Alio! house-style checks (name, word list, guarantees)")
    args = ap.parse_args()
    text = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()

    flags, triples = scan(text, args.limit, args.alio)
    if not flags and triples < 3:
        print("No surface tells found. Now check the construction tells in SKILL.md.")
        return
    for n, cat, hit, tip in flags:
        print(f"line {n:>3}  {cat:<8} {hit!r}: {tip}")
    if triples >= 3:
        print(f"\n{triples} lists of three found. AI leans on triplets; keep only the ones listing real things.")
    counts = {}
    for _, cat, _, _ in flags:
        counts[cat] = counts.get(cat, 0) + 1
    print("\nSummary: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print("Surface tells are the weakest signal. Fix the construction tells first.")


if __name__ == "__main__":
    main()
