# 🧼 Lab 11: Linear History, Interactive Rebasing & Cherry-Picking

> **Objective**: Master history crafting using interactive rebasing (`git rebase -i`); squash messy interim commits; reword commit messages; and surgically backport individual commits using `git cherry-pick`.

---

## 📋 Prerequisites
1. Completion of Lab 10.
2. Clean working tree on `main` (`git status` shows clean).
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Crafting a Coherent Commit Narrative

When building complex algorithms, engineers rarely write perfect code in one sitting. You might make 4 interim commits:
`"WIP"`, `"fix typo"`, `"forgot semicolon"`, `"now it works"`.

Pushing this chaotic history to a shared team branch burdens code reviewers. **Interactive Rebasing (`git rebase -i`)** allows you to rewrite your local history *before* pushing, squashing messy commits into a single cohesive story.

**`git cherry-pick`** allows you to select a single commit from one branch and apply its exact changes to another branch without merging the entire branch.

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 11.1: Simulate a Messy Feature Branch
Create a topic branch for a sensor calibration utility:

```powershell
git switch -c feature/sensor-calibrator
```

Make three small, messy commits in `src/calculator.py`:

```powershell
# Commit 1
Add-Content -Path src/calculator.py -Value "`ndef calibrate_sensor(val):`n    return val * 1.05"
git commit -am "WIP: sensor calibration formula"

# Commit 2 (Fixing formatting)
Add-Content -Path src/calculator.py -Value "# Calibration constant updated"
git commit -am "fix: add calibration comment"

# Commit 3 (Adding docstring)
Add-Content -Path src/calculator.py -Value "# Ready for robot test"
git commit -am "docs: note calibration readiness"
```

Inspect the messy log:
```powershell
git log -n 3 --oneline
```

---

### Task 11.2: Interactive Rebasing (`git rebase -i`)
Launch interactive rebase for the last 3 commits:

```powershell
git rebase -i HEAD~3
```

Git opens your default editor (e.g. VS Code or Notepad) displaying the rebase instruction sheet:
```text
pick 1a2b3c4 WIP: sensor calibration formula
pick 2b3c4d5 fix: add calibration comment
pick 3c4d5e6 docs: note calibration readiness

# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# d, drop = remove commit
```

Modify the sheet to keep the first commit and **squash (`s`)** the following two into it:
```text
pick 1a2b3c4 WIP: sensor calibration formula
squash 2b3c4d5 fix: add calibration comment
squash 3c4d5e6 docs: note calibration readiness
```

Save and close the file. Git combines all three and prompts for a final, clean commit message:
```text
feat(sensor): implement robot sensor calibration routine

Combines initial multiplier with validation comments and documentation.
```

Save and exit. Check your new linear history:
```powershell
git log -n 1 --stat
```
The three messy commits are now transformed into a single professional commit!

---

### Task 11.3: Cherry-Picking a Specific Commit
Now switch to `main`:
```powershell
git switch main
```

Suppose `feature/sensor-calibrator` is still experimental, but you urgently need just that calibration commit on `main`.

Find the SHA of the squashed commit on `feature/sensor-calibrator`:
```powershell
git log feature/sensor-calibrator -n 1 --oneline
# Example: 8f9e0a1
```

Apply ONLY that commit onto `main`:
```powershell
git cherry-pick 8f9e0a1
```

**Expected Output:**
```text
[main b1c2d3e] feat(sensor): implement robot sensor calibration routine
 Date: ...
 1 file changed, 4 insertions(+)
```
The commit has been transplanted onto `main` with zero collateral baggage!

Clean up the feature branch:
```powershell
git branch -D feature/sensor-calibrator
```

---

## 🔍 Verification Steps
1. Run `git log -n 2 --oneline` on `main` — verify the cherry-picked commit exists at `HEAD`.
2. Run `python -m unittest discover tests` — all unit tests pass with `OK`.
3. Discard the test additions to keep `src/calculator.py` pristine:
```powershell
git reset --hard HEAD~1
```

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| Rebase conflict | Changes collided during re-application. | Resolve markers in file, run `git add <file>`, then run `git rebase --continue`. |
| Rebasing pushed shared commits | Violates Golden Rule of Rebasing. | Only rebase local private branches. Never rebase shared remote branches. |
| Cherry-pick failure | Commit depends on earlier code that doesn't exist on active branch. | Ensure dependencies are present, or resolve conflict during cherry-pick. |

---

## ✅ Completion Checklist
- [ ] Created multiple interim commits on a topic branch.
- [ ] Executed `git rebase -i` and squashed commits into an atomic unit.
- [ ] Reworded the consolidated commit message cleanly.
- [ ] Transferred a single commit across branches using `git cherry-pick`.
- [ ] Understood when to squash (before pushing) and when NOT to rebase (public branches).

