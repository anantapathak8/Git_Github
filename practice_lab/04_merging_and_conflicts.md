# ⚔️ Lab 04: Merging Strategies & Conflict Resolution

> **Objective**: Understand Fast-Forward vs 3-Way merges, execute clean integrations, orchestrate an authentic, genuinely reproducible merge conflict, resolve it using CLI tools, and test the resulting codebase.

---

## 📋 Prerequisites
1. Completion of Lab 03 (feature branch `feature/robot-telemetry` exists with unmerged commit).
2. Clean working tree on `main` (`git status` shows clean).
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Merge Algorithms in Git

When combining branches, Git evaluates the commit graph:

1. **Fast-Forward (FF)**: If no commits occurred on the target branch (`main`) after the feature branch was split, Git simply moves the pointer forward. No new merge commit is generated.
2. **3-Way Merge (`ORT` Strategy)**: If both branches progressed independently, Git locates their **Lowest Common Ancestor (Base)**, compares both tips against it, and generates a new **Merge Commit** with two parent references.

```
Fast-Forward:
main:     A --- B
                 \
feature:          C --- D
Result:   A --- B --- C --- D (main, feature)

3-Way Merge:
main:     A --- B --------- M (Merge Commit)
                 \         /
feature:          C --- D /
```

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 4.1: Perform a Fast-Forward Merge
Switch to `main` and integrate `feature/robot-telemetry`:

```powershell
git switch main
git merge feature/robot-telemetry
```

**Expected Output:**
```text
Updating b2c3d4e..7a8b9c0
Fast-forward
 src/calculator.py        | 16 ++++++++++++++++
 tests/test_calculator.py |  7 +++++++
 2 files changed, 23 insertions(+)
```

Verify tests on `main`:
```powershell
python -m unittest discover tests
```

---

### Task 4.2: Engineer a Planned Merge Conflict (100% Reproducible)

Let's intentionally engineer a collision on the `format_multiline_banner` function in `src/greeting.py`.

#### Step 1: Branch Alpha (`feature/banner-v1`)
Create branch `feature/banner-v1`:
```powershell
git switch -c feature/banner-v1
```

Open `src/greeting.py`, locate `format_multiline_banner`, and modify the banner border to use `#` characters:
```python
def format_multiline_banner(name: str, project_name: str = "Robotics & AI Lab") -> str:
    clean_name = _validate_name(name)
    line = "#" * 50
    return (
        f"{line}\n"
        f"  [ALPHA] PROJECT: {project_name.upper()}\n"
        f"  OPERATOR: {clean_name}\n"
        f"{line}"
    )
```

Commit Branch Alpha:
```powershell
git add src/greeting.py
git commit -m "feat(greeting): enhance banner using 50-hash border"
```

---

#### Step 2: Branch Beta (`feature/banner-v2`)
Switch back to `main`:
```powershell
git switch main
```

Create Branch Beta from `main`:
```powershell
git switch -c feature/banner-v2
```

In `src/greeting.py`, edit the EXACT SAME lines in `format_multiline_banner` to use `*` characters:
```python
def format_multiline_banner(name: str, project_name: str = "Robotics & AI Lab") -> str:
    clean_name = _validate_name(name)
    line = "*" * 50
    return (
        f"{line}\n"
        f"  [BETA] PROJECT: {project_name.upper()}\n"
        f"  OPERATOR: {clean_name}\n"
        f"{line}"
    )
```

Commit Branch Beta:
```powershell
git add src/greeting.py
git commit -m "feat(greeting): update banner with 50-star border"
```

---

#### Step 3: Trigger the Collision
Switch to `main` and merge Branch Alpha:
```powershell
git switch main
git merge feature/banner-v1
```
*(Merges cleanly via Fast-Forward).*

Now attempt to merge Branch Beta into `main`:
```powershell
git merge feature/banner-v2
```

**Git stops execution and reports a conflict!**
```text
Auto-merging src/greeting.py
CONFLICT (content): Merge conflict in src/greeting.py
Automatic merge failed; fix conflicts and then commit the result.
```

---

### Task 4.3: Inspect Conflict State
Run `git status` in PowerShell:
```powershell
git status
```

**Expected Output:**
```text
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   src/greeting.py
```

Open `src/greeting.py`. You will see the authentic Git conflict markers:
```python
<<<<<<< HEAD
    line = "#" * 50
    return (
        f"{line}\n"
        f"  [ALPHA] PROJECT: {project_name.upper()}\n"
        f"  OPERATOR: {clean_name}\n"
        f"{line}"
    )
=======
    line = "*" * 50
    return (
        f"{line}\n"
        f"  [BETA] PROJECT: {project_name.upper()}\n"
        f"  OPERATOR: {clean_name}\n"
        f"{line}"
    )
>>>>>>> feature/banner-v2
```

---

### Task 4.4: Emergency Abort Demonstration
Before resolving, practice the emergency escape hatch:
```powershell
git merge --abort
```

Verify that the working tree is instantly restored:
```powershell
git status
```
Output: `nothing to commit, working tree clean`.

---

### Task 4.5: Re-trigger and Resolve the Conflict
Re-trigger the merge:
```powershell
git merge feature/banner-v2
```

Resolve `src/greeting.py` by removing all markers (`<<<<<<<`, `=======`, `>>>>>>>`) and authoring a unified hybrid implementation:
```python
def format_multiline_banner(name: str, project_name: str = "Robotics & AI Lab") -> str:
    clean_name = _validate_name(name)
    line = "=" * 50
    return (
        f"{line}\n"
        f"  PROJECT: {project_name.upper()}\n"
        f"  OPERATOR: {clean_name}\n"
        f"  STATUS: READY FOR VERSION CONTROL EXERCISE\n"
        f"{line}"
    )
```

Run test suite to verify code syntax and integrity:
```powershell
python -m unittest discover tests
```

Stage the resolved file:
```powershell
git add src/greeting.py
```

Finalize the merge commit:
```powershell
git commit -m "merge(greeting): resolve banner styling conflict with unified layout"
```

Clean up feature branches:
```powershell
git branch -d feature/banner-v1
git branch -d feature/banner-v2
git branch -d feature/robot-telemetry
```

---

## 🔍 Verification Steps
1. Run `git log --graph --oneline -n 6` — verify the merge commit node displaying two parents.
2. Run `git status` — must show `working tree clean`.
3. Run `python -m unittest discover tests` — all unit tests pass with `OK`.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| Committing conflict markers into production | Leaving `<<<<<<<` or `>>>>>>>` inside the file. | Search codebase for `<<<<<<<` before staging. Run `git diff` to verify clean syntax. |
| Forgetting to run `git commit` after `git add` | Believing staging concludes the merge. | Run `git commit` to finalize and record the merge commit. |
| Panicking during complex merge | Too many files in conflict. | Run `git merge --abort` to return safely to the clean pre-merge state. |

---

## ✅ Completion Checklist
- [ ] Executed a Fast-Forward merge of `feature/robot-telemetry`.
- [ ] Created two diverging branches (`feature/banner-v1` and `feature/banner-v2`).
- [ ] Triggered a genuine merge conflict on `src/greeting.py`.
- [ ] Demonstrated aborting a merge cleanly with `git merge --abort`.
- [ ] Re-merged, removed conflict markers, and synthesized a clean resolution.
- [ ] Verified tests pass and committed the merge.
- [ ] Deleted merged feature branches.
