"""Helper for run.sh: prepare prompts, extract answers, blind them for the judge, summarise.

Subcommands:
  prepare <out> <superpowers-skills> <lens-root> <task>...   write prompts/<task>-<arm>.md
  extract <out>                                             <run>.json -> <run>.md + <run>.meta.json
  blind <out>                                               answers -> judge/<id>.prompt.md (+ key.json)
  summarize <out>                                           per task and arm: hit rates, cost, length
"""
import glob
import json
import os
import random
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LENSES = ("software-design", "clean-python", "data-intensive")
ARMS = ("bare", "lens")


def render(template, **values):
    for k, v in values.items():
        template = template.replace("{{" + k + "}}", v)
    assert "{{" not in template, "unfilled placeholder"
    return template


def read_block(task, arm, sp, root):
    sp_files = {
        "v1": ["brainstorming/SKILL.md", "writing-plans/SKILL.md"],
        "v2": ["requesting-code-review/code-reviewer.md"],
        "v3": ["systematic-debugging/SKILL.md"],
        "v4": ["brainstorming/SKILL.md"],
    }[task]
    lines = [f"- {sp}/{f}" for f in sp_files]
    if arm == "lens":
        if task == "v1":
            lines.append(f"- {root}/software-design/references/coordination.md (shared by the lenses; read this one copy)")
            for l in LENSES:
                lines += [f"- {root}/{l}/SKILL.md", f"- {root}/{l}/references/superpowers-hooks.md (the brainstorming and writing-plans sections)",
                          f"- {root}/{l}/assets/spec-sections.md"]
        elif task == "v3":
            lines.append(f"- {root}/software-design/references/coordination.md (shared by the lenses; read this one copy)")
            for l in LENSES:
                lines += [f"- {root}/{l}/SKILL.md", f"- {root}/{l}/references/superpowers-hooks.md (the systematic-debugging section)"]
        elif task == "v4":
            lines += [f"- {root}/{l}/SKILL.md" for l in LENSES]
    return "\n".join(lines)


def prepare(out, sp, root, tasks):
    os.makedirs(os.path.join(out, "prompts"), exist_ok=True)
    header = open(os.path.join(HERE, "tasks", "header.md")).read()
    names = {"v1": "v1-design", "v2": "v2-review", "v3": "v3-debug", "v4": "v4-bounded"}
    for task in tasks:
        body = open(os.path.join(HERE, "tasks", names[task] + ".md")).read()
        for arm in ARMS:
            lens_review = ""
            if task == "v2" and arm == "lens":
                lens_review = ", plus these files appended to it: " + ", ".join(
                    f"{root}/{l}/references/review-lens.md" for l in LENSES)
            text = render(header + body,
                          LENS_NOTE="" if arm == "bare" else ", plus the lens skills software-design, clean-python and data-intensive",
                          READ_BLOCK=read_block(task, arm, sp, root),
                          FIXTURES=os.path.join(HERE, "fixtures"),
                          LENS_REVIEW=lens_review)
            open(os.path.join(out, "prompts", f"{task}-{arm}.md"), "w").write(text)


def extract(out):
    for path in glob.glob(os.path.join(out, "runs", "*.json")):
        if path.endswith(".meta.json"):
            continue
        base = path[:-5]
        try:
            data = json.load(open(path))
        except ValueError:
            data = {}
        text = data.get("result", "") or ""
        open(base + ".md", "w").write(text)
        usage = data.get("usage", {}) or {}
        meta = {
            "cost_usd": data.get("total_cost_usd"),
            "duration_s": (data.get("duration_ms") or 0) / 1000,
            "input_tokens": sum(usage.get(k, 0) or 0 for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")),
            "output_tokens": usage.get("output_tokens"),
            "words": len(text.split()),
            "error": bool(data.get("is_error")) or not text,
        }
        json.dump(meta, open(base + ".meta.json", "w"))


REDACT = [r"software-design", r"clean-python", r"data-intensive", r"^.*Lens check:.*$", r"\blens(es)?\b",
          r"Ousterhout", r"Kleppmann", r"Anaya", r"coordination\.md", r"superpowers-hooks\.md", r"review-lens\.md",
          r"spec-sections\.md", r"Philosophy of Software Design", r"Designing Data-Intensive Applications", r"Clean Code in Python"]


def blind(out):
    """Write one judge prompt per answer, with lens vocabulary removed and a random id, so the judge can't tell the arms apart."""
    jdir = os.path.join(out, "judge")
    os.makedirs(jdir, exist_ok=True)
    key = {}
    template = open(os.path.join(HERE, "judge.md")).read()
    for path in sorted(glob.glob(os.path.join(out, "runs", "*.md"))):
        run = os.path.basename(path)[:-3]
        task = run.split("-")[0]
        text = open(path).read()
        for pattern in REDACT:
            text = re.sub(pattern, "[redacted]", text, flags=re.I | re.M)
        rid = "%08x" % random.getrandbits(32)
        key[rid] = run
        answer = os.path.join(jdir, rid + ".answer.md")
        open(answer, "w").write(text)
        rubric = json.load(open(os.path.join(HERE, "rubrics", {"v1": "v1-design", "v2": "v2-review", "v3": "v3-debug", "v4": "v4-bounded"}[task] + ".json")))
        fixture = {"v1": "", "v2": "v2-diff.md", "v3": "v3-incident.md", "v4": "v4-cli.md"}[task]
        prompt = render(template,
                        CONTEXT=rubric["context"],
                        FIXTURE=(f"The material the answer is about: {os.path.join(HERE, 'fixtures', fixture)}" if fixture else "There is no separate material; the rubric describes the request."),
                        ITEMS="\n".join(f"- {k}: {v}" for k, v in rubric["items"].items()),
                        FP=("Also count false_positives: findings that make a factually wrong claim about the code. List each briefly." if rubric["false_positives"] else "Set false_positives to 0."),
                        ANSWER=answer)
        open(os.path.join(jdir, rid + ".prompt.md"), "w").write(prompt)
    json.dump(key, open(os.path.join(jdir, "key.json"), "w"), indent=1)


def grades(out):
    key = json.load(open(os.path.join(out, "judge", "key.json")))
    result = {}
    for rid, run in key.items():
        path = os.path.join(out, "judge", rid + ".json")
        try:
            data = json.load(open(path))
            text = data.get("result", "")
            result[run] = json.loads(re.search(r"\{.*\}", text, re.S).group(0))
        except (OSError, ValueError, AttributeError):
            result[run] = None
    return result


def summarize(out):
    g = grades(out)
    rows = {}
    for meta_path in glob.glob(os.path.join(out, "runs", "*.meta.json")):
        run = os.path.basename(meta_path)[: -len(".meta.json")]
        task, arm, _ = run.split("-")
        rows.setdefault((task, arm), []).append((run, json.load(open(meta_path)), g.get(run)))
    report = []
    for task in sorted({t for t, _ in rows}):
        rubric = json.load(open(os.path.join(HERE, "rubrics", {"v1": "v1-design", "v2": "v2-review", "v3": "v3-debug", "v4": "v4-bounded"}[task] + ".json")))
        items = list(rubric["items"])
        report.append(f"\n## {task}: {rubric['context']}\n")
        report.append("| item | " + " | ".join(ARMS) + " |")
        report.append("|---|" + "---|" * len(ARMS))
        for item in items:
            cells = []
            for arm in ARMS:
                graded = [gr for _, _, gr in rows.get((task, arm), []) if gr]
                hits = sum(1 for gr in graded if gr.get("items", {}).get(item, {}).get("hit"))
                cells.append(f"{hits}/{len(graded)}")
            report.append(f"| {item} | " + " | ".join(cells) + " |")
        for label, fn in [
            ("mean items hit", lambda r: statistics.mean(sum(1 for v in gr["items"].values() if v.get("hit")) for _, _, gr in r if gr) if any(gr for _, _, gr in r) else float("nan")),
            ("false positives (total)", lambda r: sum((gr or {}).get("false_positives", 0) or 0 for _, _, gr in r)),
            ("answer words (median)", lambda r: statistics.median(m["words"] for _, m, _ in r)),
            ("input tokens (median)", lambda r: statistics.median(m["input_tokens"] for _, m, _ in r)),
            ("cost USD (median)", lambda r: statistics.median(m["cost_usd"] or 0 for _, m, _ in r)),
            ("seconds (median)", lambda r: statistics.median(m["duration_s"] for _, m, _ in r)),
            ("runs (errors)", lambda r: f"{len(r)} ({sum(1 for _, m, _ in r if m['error'])})"),
        ]:
            cells = []
            for arm in ARMS:
                r = rows.get((task, arm), [])
                v = fn(r) if r else "-"
                cells.append(f"{v:.2f}" if isinstance(v, float) and v != int(v) else str(v))
            report.append(f"| *{label}* | " + " | ".join(cells) + " |")
        if task == "v4":
            for arm in ARMS:
                qs = []
                for run, _, _ in rows.get((task, arm), []):
                    m = re.search(r"QUESTIONS ASKED:\s*(\d+)", open(os.path.join(out, "runs", run + ".md")).read())
                    qs.append(int(m.group(1)) if m else None)
                report.append(f"\n{arm}: questions asked per run: {qs}")
    text = "\n".join(report)
    open(os.path.join(out, "summary.md"), "w").write(text + "\n")
    print(text)


if __name__ == "__main__":
    cmd, out, *rest = sys.argv[1:]
    {"prepare": lambda: prepare(out, rest[0], rest[1], rest[2:]),
     "extract": lambda: extract(out),
     "blind": lambda: blind(out),
     "summarize": lambda: summarize(out)}[cmd]()
