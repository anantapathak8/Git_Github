# 🎯 Lab 02: Staging Mechanics & Commit Mastery

> **Objective**: Master the distinction between working directory, staging area, and repository; use granular diffs (`git diff` vs `git diff --staged`); practice interactive partial staging (`git add -p`); and craft atomic conventional commits with amendments.

---

## 📋 Prerequisites
1. Completion of Lab 01 (repository initialized and initial commit created on `main`).
2. Clean working tree (`git status` shows `nothing to commit, working tree clean`).
3. Python test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Why the Staging Area is Git's Superpower

Unlike Subversion or Mercurial where committing immediately snapshots all modified files, Git's **Staging Area (Index)** acts as a craftsperson's workbench:

```
[ Working Tree ]  ====== git diff ======>  [ Staging Area ]  ====== git diff --staged ======>  [ HEAD Commit ]
(Raw Edits)                                 (Curated Snapshot)                                   (Permanent History)
```

This staging decoupling allows you to:
- Make 10 changes across 5 files, but group them into 3 distinct, atomic commits.
- Review your exact diff character-by-character before freezing it into the project history.
- Exclude accidental debug prints or scratch lines from production commits.

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 2.1: Inspect Differences Before and After Staging

Let's modify `src/calculator.py` by adding a new mathematical function:

Open `src/calculator.py` and append:
```python
def absolute_value(x: Number) -> Number:
    """Return the non-negative magnitude of a number.

    Args:
        x: Numeric operand.

    Returns:
        Absolute magnitude of x.
    """
    _validate_numeric(x, "Value 'x'")
    return abs(x)
```

Now run `git status` in PowerShell:
```powershell
git status
```

**Expected Output:**
```text
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   src/calculator.py

no changes added to commit (use "git add" to track)
```

Inspect the unstaged diff:
```powershell
git diff
```
Notice green lines showing the newly added lines.

Now stage the file:
```powershell
git add src/calculator.py
```

Run `git diff` again:
```powershell
git diff
```
*It prints nothing!* Because `git diff` compares your **working directory** against the **staging area**. Since both now match, the diff is empty.

To view what is currently staged:
```powershell
git diff --staged
```
*(Synonym: `git diff --cached`)*  
Now you see the staged additions against `HEAD`!

---

### Task 2.2: Interactive Staging (`git add -p`)

What if you made two unrelated changes in the same file and want them in separate commits? Git provides patch mode (`--patch` or `-p`):

Add two distinct changes in `tests/test_calculator.py`:
1. Add a comment at the top: `# Author: Robotics Team 2026`
2. Add a test method inside `TestCalculatorBasicOperations`:
```python
    def test_absolute_value(self):
        """Verify magnitude calculation."""
        from src.calculator import absolute_value
        self.assertEqual(absolute_value(-42), 42)
        self.assertEqual(absolute_value(3.14), 3.14)
```

Run interactive patch staging:
```powershell
git add -p tests/test_calculator.py
```

Git breaks the file into logical hunks and prompts:
```text
Stage this hunk [y,n,q,a,d,s,e,?]?
```
- `y`: stage this hunk
- `n`: do not stage this hunk
- `s`: split current hunk into smaller hunks
- `e`: manually edit hunk
- `q`: quit

Press `y` to stage the hunk.

---

### Task 2.3: Commit with Conventional Format
Stage all changes for the absolute value feature:
```powershell
git add src/calculator.py tests/test_calculator.py
git commit -m "feat(calc): add absolute_value function with numeric type checks"
```

**Expected Output:**
```text
[main 4a5b6c7] feat(calc): add absolute_value function with numeric type checks
 2 files changed, 18 insertions(+)
```

---

### Task 2.4: Amending the Last Commit (`git commit --amend`)
Suppose immediately after committing, you notice you forgot to update `CHANGELOG.md`.

Instead of creating a messy follow-up commit ("fix typo"), you can amend the previous commit:

Edit `CHANGELOG.md` to add `absolute_value` under `[Unreleased]`:
```markdown
- Added `absolute_value` function to calculator module.
```

Stage the forgotten file:
```powershell
git add CHANGELOG.md
```

Amend the previous commit without creating a duplicate commit:
```powershell
git commit --amend -m "feat(calc): implement absolute_value and document in changelog"
```

Inspect the log:
```powershell
git log -n 1 --stat
```

**Expected Output:**
```text
commit b2c3d4e (HEAD -> main)
Author: Your Name <your.email@university.edu>
Date:   ...

    feat(calc): implement absolute_value and document in changelog

 CHANGELOG.md             |  1 +
 src/calculator.py        | 10 ++++++++++
 tests/test_calculator.py |  7 +++++++
 3 files changed, 18 insertions(+)
```

> ⚠️ **Critical Rule**: Only amend commits that exist locally. Never amend a commit that has already been pushed to a remote shared branch, as it rewrites commit history.

---

## 🔍 Verification Steps
1. Run `python -m unittest discover tests` — all tests must pass.
2. Run `git status` — verify working tree is clean.
3. Run `git log -1 --stat` — verify that `CHANGELOG.md`, `calculator.py`, and `test_calculator.py` are part of a single amended commit.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `git diff` shows no output after `git add` | Changes have already been staged. | Use `git diff --staged` to view staged changes. |
| Amending accidentally pushed commits | Running `git commit --amend` after pushing to GitHub. | Amending rewrites the commit hash. Never amend pushed commits; use a new commit instead. |
| Accidental staging of unwanted files | Running `git add .` carelessly. | Unstage specific files using `git restore --staged <file>`. |

---

## ✅ Completion Checklist
- [ ] Practiced viewing unstaged changes with `git diff`.
- [ ] Practiced viewing staged changes with `git diff --staged`.
- [ ] Used interactive patch mode with `git add -p`.
- [ ] Created an atomic commit following Conventional Commits.
- [ ] Staged an additional file and amended the commit using `git commit --amend`.
- [ ] Verified tests pass and commit history is clean.
