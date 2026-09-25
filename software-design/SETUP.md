# Setting up the superpowers lenses in a repo

<!-- setup:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
The three lenses (software-design, clean-python, data-intensive) supply judgment inside [superpowers](https://github.com/obra/superpowers) steps. They don't run on their own, and nothing in superpowers loads them, so each repo has to wire them in. This file is the same in every lens folder.

## 1. Pick the lenses

| Lens | Install when the repo… |
|---|---|
| software-design | has modules and interfaces worth designing (most repos) |
| clean-python | contains Python code |
| data-intensive | stores data with concurrency, scale, migrations, queues, caches or several stores |

Install any subset. The lenses share `references/coordination.md` and skip the rules of any lens that isn't installed.

## 2. Require superpowers in the repo

Add to `<repo>/.claude/settings.json` and commit:

```json
{
  "extraKnownMarketplaces": {
    "superpowers-marketplace": {
      "source": { "source": "github", "repo": "obra/superpowers-marketplace" }
    }
  },
  "enabledPlugins": {
    "superpowers@superpowers-marketplace": true
  }
}
```

A developer without the plugin installs it with `/plugin install superpowers@superpowers-marketplace`. The lenses were tested with superpowers **6.4.1**.

## 3. Install the lenses

Copy each chosen lens folder into `<repo>/.claude/skills/` and commit it, so everyone who clones the repo gets the same lenses:

```bash
cp -R <lens-repo>/software-design <lens-repo>/clean-python <repo>/.claude/skills/
```

For personal use across all your repos, copy them to `~/.claude/skills/` instead. Pick one location per lens so only one copy loads. Keep every installed lens on the same lens-repo commit: their `references/coordination.md` files must be identical.

## 4. Add the lens block to the repo's CLAUDE.md

```markdown
## Superpowers lenses
Installed lenses: software-design, clean-python, data-intensive
- At every superpowers step (brainstorming, writing-plans, test-driven-development,
  subagent-driven-development / executing-plans, verification-before-completion,
  requesting- / receiving-code-review, systematic-debugging,
  finishing-a-development-branch), read `references/coordination.md` once and the step's
  `references/steps/<step>.md` (one copy each, from any installed lens).
- A lens not listed above isn't installed: skip its rules.

### Repo facts for the lenses
- Python: 3.12 · uv · ruff check · ruff format --check · mypy --strict src · pytest -q
- Database: Postgres 16 at READ COMMITTED; migrations with Alembic
- Queues, caches, other stores: none
```

- Edit the "Installed lenses" line to match what you copied.
- Keep only the fact lines for installed lenses: the Python line for clean-python, the others for data-intensive. software-design needs none.
- Replace the example values with the repo's real ones. Update them when they change; they stop brainstorming from rediscovering the same facts every session.

## 5. Check the setup

```bash
bash .claude/skills/software-design/scripts/check-superpowers.sh
```

Every lens ships the same script; run it from any installed lens.
- **OK:** the installed superpowers has every anchor the lenses hook into.
- **OK (with warning):** the anchors are present, but the version differs from the tested one.
- **FAIL:** superpowers changed where the lenses hook in. Don't rely on the lenses until the lens repo is updated.

Then open a fresh session and try one prompt for each installed lens:

| Prompt | Expected |
|---|---|
| "Build a new <feature> service" | Brainstorming leads. The spec keeps brainstorming's headings, with lens subsections under them. The plan's Global Constraints carry the lens rules. |
| A one-file fix to existing code | Brainstorming's bounded path. After the change: `Lens check: …`, with one segment per installed lens that applies. |
| "Review the architecture of this repo" / "Is this module Pythonic?" / "Postgres or DynamoDB for this?" | A software-design audit, a clean-python review, or a data-intensive decision (the matching lens). |

## Updating

- **After a superpowers update:** rerun `check-superpowers.sh`.
- **To update the lenses:** copy the folders again from the lens repo, all from the same commit.
<!-- setup:end -->
