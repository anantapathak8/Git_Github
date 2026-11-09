# ⚔️ The Definitive Merge Conflict Guide: Diagnosis, Resolution & Prevention

> **Robotics & AI B.Tech Curriculum — Week 3 Lab**  
> *"Merge conflicts are not errors or disasters; they are Git asking for human intelligence when automated heuristics cannot decide."*

---

## 🎯 Objective
Master the diagnosis, anatomy, and resolution of merge conflicts; deliberately engineer an authentic, 100% reproducible conflict on Python source code; resolve it using CLI tools; verify post-merge test integrity; and explore prevention best practices.

---

## 📋 Prerequisites
1. Local Git repository initialized on `main` with initial commit.
2. Clean working tree (`git status` shows `working tree clean`).
3. Python unit test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: What is a Merge Conflict?

Git is remarkably adept at combining changes made concurrently by different team members. When Developer A modifies line 10 of `calculator.py` and Developer B modifies line 90 of `greeting.py`, Git merges both histories automatically using a 3-way merge algorithm.

However, a **merge conflict** occurs when:
1. **Conflicting Edits**: Two or more branches modify the **exact same line(s)** of a file in different ways since their common ancestor commit.
2. **Delete vs Modify**: One developer edits a file while another developer deletes or renames it.

In these situations, Git stops execution, leaves files in an intermediate "unmerged" state, and prompts you to resolve the conflict manually.

---

## 🧩 Anatomy of Conflict Markers

When Git encounters a collision, it inserts marker strings directly into the affected source file:

```python
<<<<<<< HEAD (Current change / Target branch)
    if clean_style == "standard":
        return f"Greetings and welcome, {clean_name}!"
=======
    if clean_style == "standard":
        return f"Salutations, {clean_name}! System ready."
>>>>>>> conflict-sim-beta (Incoming change)
```

### Breaking Down the Markers:
- `<<<<<<< HEAD`: Marks the start of the conflicting section. Shows the version of code currently checked out on your active branch (e.g., `main`).
- `=======`: The separator dividing the two contradictory implementations.
- `>>>>>>> <branch_name>`: Marks the end of the conflict block and specifies the incoming branch or commit ID.

---

## 💻 Step-by-Step Instructions & Exact Commands (100% Reproducible)

### Step 1: Ensure Clean Main Branch
In PowerShell:
```powershell
git switch main
git status
```

---

### Step 2: Create Branch Alpha (Modify Standard Greeting)
```powershell
git switch -c conflict-sim-alpha
```

Open `src/greeting.py` and locate the `standard` style return statement inside `greet()`:
```python
    if clean_style == "standard":
        return f"Hello, {clean_name}!"
```

Change it to:
```python
    if clean_style == "standard":
        return f"Greetings and welcome, {clean_name}!"
```

Update test expectation in `tests/test_greeting.py` (lines 29 & 59) to match:
```python
        self.assertEqual(result, "Greetings and welcome, Anant!")
```

Save and commit:
```powershell
python -m unittest discover tests
git add src/greeting.py tests/test_greeting.py
git commit -m "feat(greeting): make standard greeting more formal and welcoming"
```

---

### Step 3: Create Branch Beta from Main (Contradictory Change)
Switch back to `main`:
```powershell
git switch main
```

Create a second branch off `main`:
```powershell
git switch -c conflict-sim-beta
```

In `src/greeting.py`, locate the same `standard` style return statement and change it to something completely different:
```python
    if clean_style == "standard":
        return f"Salutations, {clean_name}! Telemetry ready."
```

Update test expectation in `tests/test_greeting.py` to match Branch Beta:
```python
        self.assertEqual(result, "Salutations, Anant! Telemetry ready.")
```

Save and commit:
```powershell
python -m unittest discover tests
git add src/greeting.py tests/test_greeting.py
git commit -m "feat(greeting): customize standard greeting for robotic telemetry"
```

---

### Step 4: Merge Branch Alpha into Main
```powershell
git switch main
git merge conflict-sim-alpha
```

**Expected Output:**
```text
Updating ...
Fast-forward
 src/greeting.py          | 2 +-
 tests/test_greeting.py   | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```
Branch Alpha is now safely integrated into `main`.

---

### Step 5: Merge Branch Beta (The Collision!)
Now attempt to merge Branch Beta into `main`:
```powershell
git merge conflict-sim-beta
```

**Git halts execution and reports the conflict!**
```text
Auto-merging src/greeting.py
CONFLICT (content): Merge conflict in src/greeting.py
Auto-merging tests/test_greeting.py
CONFLICT (content): Merge conflict in tests/test_greeting.py
Automatic merge failed; fix conflicts and then commit the result.
```

Inspect repository status:
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
	both modified:   tests/test_greeting.py
```

---

### Step 6: Step-by-Step Resolution Walkthrough

#### 1. Open `src/greeting.py`
You will see the conflict markers.
Choose a **Synthesized Hybrid Resolution**:
Delete all marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) and author:
```python
    if clean_style == "standard":
        return f"Greetings and welcome, {clean_name}! System telemetry ready."
```

#### 2. Open `tests/test_greeting.py`
Resolve the test assertions to match the hybrid resolution:
```python
        self.assertEqual(result, "Greetings and welcome, Anant! System telemetry ready.")
```

#### 3. Run Unit Tests Before Staging
```powershell
python -m unittest discover tests
```
Must return `OK`.

#### 4. Stage and Conclude Merge
```powershell
git add src/greeting.py tests/test_greeting.py
git commit -m "merge: resolve standard greeting conflict by combining welcome and telemetry status"
```

Clean up simulation branches:
```powershell
git branch -d conflict-sim-alpha
git branch -d conflict-sim-beta
```

---

## 🔍 Verification Steps
1. Run `git status` — confirm `nothing to commit, working tree clean`.
2. Run `python -m unittest discover tests` — all unit tests pass.
3. Run `git log --graph --oneline -n 5` — verify the explicit merge commit node.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| SyntaxError: invalid syntax (`<<<<<<<`) | Accidentally left conflict markers in source code. | Re-open the file, search for `<<<` or `>>>`, remove all marker lines, and re-test. |
| Merge aborted accidentally | Ran `git merge --abort`. | Simply re-run `git merge conflict-sim-beta` to resume conflict resolution. |
| Incomplete stage | Staged only one of two conflicted files. | Check `git status` to ensure all files under "Unmerged paths" are staged before running `git commit`. |

---

## ✅ Completion Checklist
- [ ] Created two diverging branches modifying identical source code lines.
- [ ] Triggered authentic merge conflict on `src/greeting.py` and `tests/test_greeting.py`.
- [ ] Inspected conflict markers and unmerged paths in `git status`.
- [ ] Authored clean hybrid resolution without leaving conflict markers.
- [ ] Verified test suite passes before concluding the merge.
- [ ] Finalized merge commit and deleted temporary simulation branches.
