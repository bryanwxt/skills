"""Print the skill list the s5 trigger scenario reads: superpowers' skills plus the three lenses, name and description only."""
import glob
import os
import re
import sys


def description(path):
    front = open(path).read().split("---")[1]
    value = re.search(r"^description:\s*(.*)$", front, re.M).group(1).strip()
    if value[:1] == "'":
        return value[1:-1].replace("''", "'")
    if value[:1] == '"':
        return value[1:-1].replace('\\"', '"')
    return value


superpowers, root = sys.argv[1], sys.argv[2]
for path in sorted(glob.glob(os.path.join(superpowers, "*", "SKILL.md"))):
    name = os.path.basename(os.path.dirname(path))
    if name in ("diagnosing-superpowers", "writing-skills"):
        continue
    print(f"- superpowers:{name}: {description(path)}")
for lens in ("software-design", "clean-python", "data-intensive"):
    print(f"- {lens}: {description(os.path.join(root, lens, 'SKILL.md'))}")
