"""Regenerate Part 4 (the rule index) of references/rules-and-checks.md from the chapter files.

Run after editing any rule in references/0*.md or references/1*.md:
    python3 scripts/build_rule_index.py
Rules are lines of the form `- **PFX-n** — text. *Why:* ... (p. N)`; indented sub-bullets are
kept when the rule text ends with ':' or 'as follows.' / 'by context.'.
"""
import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "references"
TARGET = ROOT / "rules-and-checks.md"
BEGIN, END = "<!-- BEGIN GENERATED: scripts/build_rule_index.py -->", "<!-- END GENERATED -->"
ORDER = ["PYR", "BLD", "INT", "PAT", "DED", "ORD", "SUM", "DEF", "ANL", "ABD", "PAG", "SCR", "PRO"]
TITLES = {
    "PYR": "Fundamentals", "BLD": "Building the pyramid", "INT": "Introductions",
    "PAT": "Introduction patterns", "DED": "Deduction and induction", "ORD": "Logical order",
    "SUM": "Summarizing grouped ideas", "DEF": "Defining the problem", "ANL": "Structuring the analysis",
    "ABD": "Abduction", "PAG": "On the page", "SCR": "On screen", "PRO": "In prose",
}
RULE = re.compile(r"^- \*\*([A-Z]{3})-(\d+)\*\*\s*(?:—|:|–)\s*(.*)$")
PAGE = re.compile(r"\((pp?\.\s*[^)]*?|Preface[^)]*|Part One intro[^)]*)\)\s*$")


def collect():
    rules = {}
    for path in sorted(glob.glob(str(ROOT / "[01]*.md"))):
        lines = Path(path).read_text().split("\n")
        for i, line in enumerate(lines):
            m = RULE.match(line.rstrip())
            if not m:
                continue
            pfx, num, rest = m.group(1), int(m.group(2)), m.group(3)
            cont = []
            j = i + 1
            while j < len(lines) and lines[j].startswith("  "):
                cont.append(lines[j].strip())
                j += 1
            page_match = PAGE.search(rest) or next((PAGE.search(c) for c in reversed(cont) if PAGE.search(c)), None)
            page = page_match.group(1) if page_match else ""
            text = re.split(r"\s*\*Why:?\*", rest)[0].strip()
            subs = [c for c in cont if c.startswith("- ")] if re.search(r"(follows\.|by context\.|:)$", text) else []
            rules.setdefault(pfx, []).append((num, text, page, Path(path).name, subs))
    return rules


def render(rules):
    out = []
    for pfx in ORDER:
        entries = sorted(rules.get(pfx, []))
        if not entries:
            continue
        out.append(f"### {pfx} — {TITLES[pfx]} (`{entries[0][3]}`)\n")
        for num, text, page, _, subs in entries:
            out.append(f"- **{pfx}-{num}** — {text}" + (f" — {page}" if page else ""))
            out.extend("  " + s for s in subs)
        out.append("")
    return "\n".join(out).rstrip()


def main():
    rules = collect()
    doc = TARGET.read_text()
    head, _, tail = doc.partition(BEGIN)
    _, _, after = tail.partition(END)
    TARGET.write_text(f"{head}{BEGIN}\n{render(rules)}\n{END}{after}")
    print(f"indexed {sum(len(v) for v in rules.values())} rules into {TARGET.name}")


if __name__ == "__main__":
    main()
