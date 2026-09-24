#!/usr/bin/env python3
"""Check a pyramid storyline (storyline.json) against the Minto rules that a
machine can check, and optionally print it as an indented outline.

Usage:
  python check_storyline.py storyline.json            # run the checks
  python check_storyline.py storyline.json --outline  # print the pyramid, then run the checks

Exit code 1 if any ERROR is found; WARN and INFO never fail the run.

storyline.json format
---------------------
{
  "title": "Deck title",
  "audience": "Who, what they know, what they must do",
  "intro": {
    "situation": "...", "complication": "...",
    "question": "...",  "answer": "governing thought, one sentence"
  },
  "key_line": {
    "logic": "inductive" | "deductive",
    "order": "time" | "structural" | "importance",
    "points": [
      {"point": "Full-sentence Key Line idea",
       "support": [ {"point": "...", "support": [ ... ]} ]}
    ]
  },
  "slides": [                       # optional until Phase 5
    {"type": "text" | "exhibit",
     "title": "Action title as a full sentence",
     "body": ["line", "..."],       # text slides
     "exhibit": "components|item|time_series|frequency|correlation|structure",
     "ref": "S" | "C" | "A" | "1" | "1.2" | "close" | "appendix",
     "notes": "speaker script"}
  ]
}

Only the checks a machine can do are here. The judgment tests (does each
point really summarize its children, is each group MECE) remain the job of
the model and the user.
"""
import json
import re
import sys

BLANK = re.compile(
    r"\b(there (are|is)|we (have|found|see)|key|several|a number of|various)\s+"
    r"(\d+|two|three|four|five|six|seven|several|many|some|key|main|major)?\s*"
    r"(problems?|issues?|reasons?|steps?|findings?|areas?|factors?|themes?|"
    r"recommendations?|options?|challenges?|considerations?|opportunities|points?)\b",
    re.I,
)
EXHIBIT_TYPES = {"components", "item", "time_series", "frequency", "correlation", "structure"}
CAPTION_WORDS = {"overview", "background", "agenda", "summary", "introduction",
                 "next steps", "conclusion", "appendix", "update", "status", "analysis"}

findings = []


def add(level, where, msg):
    findings.append((level, where, msg))


def words(s):
    return re.findall(r"[A-Za-z0-9$%.,'-]+", s or "")


def check_idea(text, where):
    if not text or not text.strip():
        add("ERROR", where, "empty idea")
        return
    if len(words(text)) < 4:
        add("ERROR", where, f"'{text}' reads as a label, not an idea. State it as a full sentence that raises a question.")
    if BLANK.search(text):
        add("WARN", where, f"possible intellectually blank assertion: '{text}'. State the insight instead of counting items.")


def walk(node, path, depth):
    check_idea(node.get("point", ""), path)
    kids = node.get("support", []) or []
    if len(kids) == 1:
        add("WARN", path, "a single support point is not a grouping. Merge it into the parent or find its siblings.")
    if len(kids) > 7:
        add("ERROR", path, f"{len(kids)} support points, more than an audience can hold. Regroup under fewer summaries.")
    elif len(kids) > 5:
        add("WARN", path, f"{len(kids)} support points. 3–4 is easier to absorb; consider regrouping.")
    if depth >= 3 and kids:
        add("INFO", path, "more than two levels below the Key Line. Consider moving this depth to the appendix.")
    for i, k in enumerate(kids, 1):
        walk(k, f"{path}.{i}", depth + 1)


def outline(data):
    intro = data.get("intro", {})
    print(f"# {data.get('title', '(untitled)')}\n")
    for k in ("situation", "complication", "question"):
        print(f"{k[0].upper()}: {intro.get(k, '')}")
    print(f"\n[A] {intro.get('answer', '')}")
    kl = data.get("key_line", {})
    print(f"    ({kl.get('logic', '?')}, {kl.get('order', '?')} order)")

    def rec(n, prefix, indent):
        print(f"{'    ' * indent}{prefix} {n.get('point', '')}")
        for i, k in enumerate(n.get("support", []) or [], 1):
            rec(k, f"{prefix}{i}.", indent + 1)

    for i, p in enumerate(kl.get("points", []), 1):
        rec(p, f"{i}.", 1)
    print()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)
    with open(args[0], encoding="utf-8") as f:
        data = json.load(f)
    if "--outline" in sys.argv:
        outline(data)

    # Introduction
    intro = data.get("intro", {})
    for k in ("situation", "complication", "question", "answer"):
        if not (intro.get(k) or "").strip():
            add("ERROR", "intro", f"missing {k}. SCQA needs all four elements (the Question may stay implied on the slides but must be written here).")
    if intro.get("question") and not intro["question"].strip().endswith("?"):
        add("WARN", "intro.question", "write the Question as an actual question.")
    if intro.get("answer"):
        check_idea(intro["answer"], "intro.answer")
    if not (data.get("audience") or "").strip():
        add("WARN", "audience", "no audience recorded. The Question lives in a specific audience's mind.")

    # Key Line
    kl = data.get("key_line", {})
    pts = kl.get("points", []) or []
    if len(pts) < 2:
        add("ERROR", "key_line", "the Key Line needs at least 2 points.")
    if len(pts) > 5:
        add("WARN", "key_line", f"{len(pts)} Key Line points; 3–4 is ideal, and more than 7 is unworkable.")
    logic = kl.get("logic")
    if logic not in ("inductive", "deductive"):
        add("ERROR", "key_line.logic", "state 'inductive' or 'deductive'.")
    elif logic == "deductive":
        add("INFO", "key_line.logic", "deduction at the Key Line is harder to absorb. Check whether it can be presented inductively.")
        if len(pts) > 4:
            add("ERROR", "key_line", "a deductive chain longer than 4 steps. Restructure it.")
    if kl.get("order") not in ("time", "structural", "importance"):
        add("ERROR", "key_line.order", "name the logical order: time, structural, or importance. If none fits, the grouping may not hold together.")
    for i, p in enumerate(pts, 1):
        walk(p, str(i), 1)

    # Slides
    slides = data.get("slides", []) or []
    if slides:
        n_text = n_ex = 0
        refs = set()
        for i, s in enumerate(slides, 1):
            w = f"slide {i}"
            t = s.get("type")
            title = (s.get("title") or "").strip()
            refs.add(str(s.get("ref", "")))
            if t not in ("text", "exhibit"):
                add("ERROR", w, "type must be 'text' or 'exhibit'.")
            if not title:
                add("ERROR", w, "missing action title.")
            else:
                if title.lower() in CAPTION_WORDS or len(words(title)) < 4:
                    add("ERROR", w, f"'{title}' is a caption. Use a statement of the slide's point.")
                if len(words(title)) > 15:
                    add("WARN", w, f"title has {len(words(title))} words; aim for 15 or fewer.")
                if BLANK.search(title):
                    add("WARN", w, f"title may be a blank assertion: '{title}'.")
            if t == "text":
                n_text += 1
                body = s.get("body", []) or []
                nw = sum(len(words(b)) for b in body)
                if len(body) > 6:
                    add("WARN", w, f"{len(body)} lines; text slides should have about 6 at most.")
                if nw > 30 and s.get("ref") not in ("A", "close"):
                    add("WARN", w, f"{nw} words; text slides should have about 30 at most. Split the slide or move text to the notes.")
            if t == "exhibit":
                n_ex += 1
                ex = s.get("exhibit")
                if ex not in EXHIBIT_TYPES:
                    add("ERROR", w, f"exhibit type must be one of {sorted(EXHIBIT_TYPES)}. Decide which question the chart answers.")
            if not (s.get("notes") or "").strip():
                add("INFO", w, "no speaker notes yet.")
            if "[DATA NEEDED" in json.dumps(s):
                add("INFO", w, "has a [DATA NEEDED] placeholder. List it for the user.")
        for i in range(1, len(pts) + 1):
            if not any(r == str(i) or r.startswith(f"{i}.") for r in refs):
                add("ERROR", f"key line {i}", "no slide covers this Key Line point.")
        for need in ("A",):
            if need not in refs:
                add("ERROR", "slides", "no slide carries the governing thought (ref 'A').")
        total = n_text + n_ex
        if total:
            add("INFO", "slides", f"{n_ex}/{total} exhibits ({100 * n_ex // total}%). The book leans heavily to exhibits (~90%).")

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda f: order[f[0]])
    for lvl, where, msg in findings:
        print(f"{lvl:5} [{where}] {msg}")
    errs = sum(1 for f in findings if f[0] == "ERROR")
    warns = sum(1 for f in findings if f[0] == "WARN")
    print(f"\n{errs} error(s), {warns} warning(s).", "PASS" if not errs else "FIX ERRORS BEFORE STORYBOARDING/RENDERING")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
