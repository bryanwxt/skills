# Lens rules for finishing-a-development-branch

<!-- steps-finishing:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## software-design

### finishing-a-development-branch
- Optionally list the design debt the branch revealed: location, red flag, fix.


## clean-python

### finishing-a-development-branch
- All configured checks green. Optionally list the Python debt the branch revealed.


## data-intensive

### finishing-a-development-branch
- Migrations are reversible, or have a documented roll-forward.
- Data tests pass.
- Optionally list data debt.
<!-- steps-finishing:end -->
