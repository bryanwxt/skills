"""Score a lens eval results directory: python3 score.py <results-dir>.

Automated checks catch the known failure shapes. They are hints, not verdicts:
read every flagged run, and skim the passing ones.
"""
import glob
import json
import os
import re
import sys

LABELS = {
    "s1": ["SPEC HEADINGS", "TASKS", "GLOBAL CONSTRAINTS", "REVIEW FOCUS", "DISPATCH", "TASK REVIEWER", "FINAL REVIEWER", "CONFLICTS"],
    "s2": ["REVIEWER PROMPT", "IMPLEMENTER PROMPT", "LENS FILES", "DEDUP GAP"],
    "s3a": ["DEFAULTS CHOSEN", "LENS CHECK", "SPEC HEADINGS", "GLOBAL CONSTRAINTS", "GAPS"],
    "s3b": ["DEFAULTS CHOSEN", "LENS CHECK", "SPEC HEADINGS", "GLOBAL CONSTRAINTS", "GAPS"],
    "s4": ["R1 LENS AND FLOW", "R1 OUTPUT", "R2 LENS AND FLOW", "R2 OUTPUT", "FILES OPENED"],
}
HEADINGS = ["Architecture", "Components", "Data flow", "Error handling", "Testing", "Implementation notes"]
SD, CP, DI = "software-design", "clean-python", "data-intensive"
TRIGGER = {"P1": ([CP], [DI]), "P2": ([SD], [CP, DI]), "P3": ([DI], [CP]), "P4": ([CP], [DI]),
           "P5": ([DI, CP], []), "P6": ([], [SD, CP, DI]), "P7": ([], [CP, DI]),
           "P8": ([SD, CP, DI], []), "P9": ([DI], [CP]), "P10": ([], [CP, DI])}


def sections(text, labels):
    """Split an answer into its labelled sections (label lines may carry markdown decoration)."""
    pattern = r"^[#*\s]*(" + "|".join(re.escape(l) for l in labels) + r")[*:\s]*"
    parts, current = {}, None
    for line in text.splitlines():
        m = re.match(pattern, line)  # case-sensitive: "Lens check: …" is an answer, "LENS CHECK" is the label
        if m:
            current = m.group(1).upper()
            parts[current] = line[m.end():] + "\n"
        elif current:
            parts[current] += line + "\n"
    return parts


def check(scen, text):
    """Return a list of problems for one run; empty means no automated flag."""
    if scen == "s5":
        try:
            answer = json.loads(re.search(r"\{.*\}", text, re.S).group(0))
        except (AttributeError, ValueError):
            return ["no JSON answer"]
        problems = []
        for p, (must, must_not) in TRIGGER.items():
            got = {s.split(":")[-1] for s in answer.get(p, [])}
            problems += [f"{p}: missed {m}" for m in must if m not in got]
            problems += [f"{p}: wrongly loaded {m}" for m in must_not if m in got]
        return problems

    s = sections(text, LABELS[scen])
    missing = [l for l in LABELS[scen] if l not in s]
    if missing:
        return [f"missing sections: {', '.join(missing)}"]
    problems = []
    if scen == "s1":
        positions = [s["SPEC HEADINGS"].find(h) for h in HEADINGS]
        if -1 in positions or positions != sorted(positions):
            problems.append("spec headings missing or out of order")
        for line in s["TASKS"].splitlines():
            title = re.sub(r"\([^)]*\)", "", line.split(":", 1)[-1])  # "(ruff, mypy)" doesn't make it a combined task
            if re.search(r"Task \d+\W+(add|set ?up|configure|install)\b[^\n]*(tooling|lint|type.?check|formatter)", line, re.I) and not re.search(r"\+|\band\b|\bwith\b|,", title):
                problems.append(f"standalone tooling task: {line.strip()}")
            if re.search(r"Task \d+\W+(define|add)\b[^\n]*interface", line, re.I):
                problems.append(f"standalone interface task: {line.strip()}")
        if "PLAN_OR_REQUIREMENTS" not in s["FINAL REVIEWER"]:
            problems.append("final reviewer doesn't use PLAN_OR_REQUIREMENTS")
        if re.search(r"review-lens\.md", s["TASK REVIEWER"]) and not re.search(r"\b(never|not|no)\b", s["TASK REVIEWER"], re.I):
            problems.append("per-task reviewer gets review-lens.md")
    elif scen == "s2":
        # Scan the prompt itself: when it's fenced, the controller's notes around it don't count.
        fenced = re.findall(r"```.*?\n(.*?)```", s["REVIEWER PROMPT"], re.S)
        prompt = "\n".join(fenced) if fenced else s["REVIEWER PROMPT"]
        leak = re.findall(r"review-lens\.md|review-checklist\.md|references/\w+|SKILL\.md|coordination\.md|superpowers-hooks|lens (?:rules|checklist)", prompt, re.I)
        if leak:
            problems.append(f"lens content in the per-task reviewer: {sorted(set(leak))}")
        if re.search(r"MANDATORY|Part 3", s["REVIEWER PROMPT"]):
            problems.append("hint: added a mandatory review section (check it's one concrete, task-specific risk)")
    elif scen in ("s3a", "s3b"):
        want = r"Lens check: python (ok|note)" if scen == "s3a" else r"Lens check: data (ok|note)"
        line = next((l for l in s["LENS CHECK"].splitlines() if "Lens check" in l), "")
        line = line.strip().strip("`")
        if not re.fullmatch(want, line):
            problems.append(f"lens-check line is {line!r}")
    elif scen == "s4":
        if DI not in s["R1 LENS AND FLOW"] or not re.search(r"technology choice|Flow A", s["R1 LENS AND FLOW"], re.I):
            problems.append("R1 not routed to data-intensive's technology-choice flow")
        if not re.search(r"quick|decision|spike", s["R1 LENS AND FLOW"], re.I):
            problems.append("R1 path not announced")
        if SD not in s["R2 LENS AND FLOW"] or "audit" not in s["R2 LENS AND FLOW"].lower():
            problems.append("R2 not routed to the software-design audit")
        if "design-review.md" not in s["R2 OUTPUT"]:
            problems.append("R2 output path isn't docs/superpowers/reviews/…-design-review.md")
    return problems


def main(results):
    runs = sorted(glob.glob(os.path.join(results, "s*-[0-9]*.md")))
    by_scen = {}
    for path in runs:
        scen = os.path.basename(path).rsplit("-", 1)[0]
        by_scen.setdefault(scen, []).append((path, check(scen, open(path).read())))
    for scen, rows in sorted(by_scen.items()):
        clean = sum(1 for _, p in rows if not p)
        print(f"{scen}: {clean}/{len(rows)} runs with no flags")
        for path, problems in rows:
            for p in problems:
                print(f"   {os.path.basename(path)}: {p}")
    print("Flags are hints. Read every flagged run, and skim the clean ones.")


if __name__ == "__main__":
    main(sys.argv[1])
