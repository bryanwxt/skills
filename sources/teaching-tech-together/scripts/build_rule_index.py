"""Regenerate the rule index in references/rules-and-checks.md from the chapter files.

Run after editing any rule in references/[01]*.md:
    python3 scripts/build_rule_index.py
Rules are lines of the form `- **PFX-n** — text. *Why:* ... (§N.k)`. Prefixes are grouped
in chapter-file order; each group is titled with its file's H1.
"""
import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "references"
TARGET = ROOT / "rules-and-checks.md"
BEGIN, END = "<!-- BEGIN GENERATED: scripts/build_rule_index.py -->", "<!-- END GENERATED -->"
RULE = re.compile(r"^- \*\*([A-Z]{3})-(\d+)\*\*\s*(?:—|:|–)\s*(.*)$")
CITE = re.compile(r"\(([^()]*)\)\s*\.?\s*$")  # final parenthetical: §N.k, Ch N intro, or appendix


def collect():
    groups = []  # (prefix, file, title, [(num, text, cite)])
    for path in sorted(glob.glob(str(ROOT / "[01][0-9]-*.md"))):
        lines = Path(path).read_text().split("\n")
        title = next((l[2:].strip() for l in lines if l.startswith("# ")), Path(path).stem)
        found = {}
        for line in lines:
            m = RULE.match(line.rstrip())
            if not m:
                continue
            pfx, num, rest = m.group(1), int(m.group(2)), m.group(3)
            cite = CITE.search(rest)
            text = re.split(r"\s*\*Why:?\*", rest)[0].strip()
            found.setdefault(pfx, []).append((num, text, cite.group(1) if cite else ""))
        for pfx, rules in found.items():
            groups.append((pfx, Path(path).name, title, sorted(rules)))
    return groups


def render(groups):
    out = []
    for pfx, name, title, rules in groups:
        out.append(f"### {pfx} — {title} (`{name}`)\n")
        out.extend(f"- **{pfx}-{n}** — {t}" + (f" — {c}" if c else "") for n, t, c in rules)
        out.append("")
    return "\n".join(out).rstrip()


def main():
    groups = collect()
    doc = TARGET.read_text()
    head, _, tail = doc.partition(BEGIN)
    _, _, after = tail.partition(END)
    TARGET.write_text(f"{head}{BEGIN}\n{render(groups)}\n{END}{after}")
    print(f"indexed {sum(len(g[3]) for g in groups)} rules into {TARGET.name}")


if __name__ == "__main__":
    main()
