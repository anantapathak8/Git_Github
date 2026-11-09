# 🕵️ Lab 09: History Investigation, Git Blame & Bisect Debugging

> **Objective**: Master code forensics using advanced `git log` filters, investigate line-by-line attribution with `git blame`, and execute binary search regression hunting using `git bisect` automated with Python unit tests.

---

## 📋 Prerequisites
1. Completion of Lab 08.
2. Clean working tree on `main` in `Git_GitHub_Week03`.
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Git as an Investigation Engine

In production engineering, discovering *when* and *why* a bug was introduced is often 80% of the debugging challenge. Git is not just for tracking code; it is a time-indexed forensic database.

Three essential forensic tools:
1. **`git log` Pickaxe (`-S`)**: Finds the exact commit that introduced or removed a specific identifier or string.
2. **`git blame`**: Displays line-by-line author, commit hash, and timestamp for any file.
3. **`git bisect`**: Uses binary search algorithm (`O(log n)`) to test intermediate commits and pinpoint the exact commit that broke the build.

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 9.1: Forensic Filtering with `git log`

Run these forensic searches in PowerShell:

```powershell
# 1. Search commits by message keyword
git log --grep="telemetry" --oneline

# 2. Search commits that modified a specific file
git log --oneline src/calculator.py

# 3. View the full patch diff introduced by commits to greeting.py
git log -p -n 2 src/greeting.py

# 4. The Pickaxe (-S): Find which commit added the string "euclidean_distance"
git log -S "euclidean_distance" --oneline

# 5. Filter commits by author
git log --author="Alice" --oneline

# 6. Filter commits by date range
git log --since="1.day.ago" --oneline
```

---

### Task 9.2: Line Attribution with `git blame`
When investigating why a specific line exists, use `git blame`:

```powershell
# Blame the entire calculator module
git blame src/calculator.py

# Inspect a specific line range (lines 20 through 35)
git blame -L 20,35 src/calculator.py
```

**Expected Output Format:**
```text
9d4e12a (Your Name 2026-11-09 18:48:31 +0530 20) def subtract(a: Number, b: Number) -> Number:
9d4e12a (Your Name 2026-11-09 18:48:31 +0530 21)     """Return the arithmetic difference of two numbers (a - b).
...
```
Each line shows:
`[Commit Hash] (Author Name, Date & Time, Line Number) Code Content`

To inspect the full commit that created that line:
```powershell
git show 9d4e12a
```

---

### Task 9.3: Automated Regression Hunting with `git bisect`

Imagine you have 500 commits between release `v1.0.0` (which worked) and `HEAD` (where tests fail). Testing each commit manually takes hours. `git bisect` performs binary search, testing only `log2(500) ≈ 9` commits!

Let's simulate this:

#### Step 1: Note the Known Good Commit
Find your root commit SHA:
```powershell
git log --reverse --oneline
# Example: 9d4e12a
```

#### Step 2: Introduce a Subtle Bug on a Test Branch
```powershell
git switch -c bisect-simulation
```

Edit `src/calculator.py` to corrupt `divide`:
```python
def divide(a: Number, b: Number) -> float:
    # BUG: Accidental plus instead of divide
    return a + b
```

Commit the bug:
```powershell
git add src/calculator.py
git commit -m "refactor(calc): optimize division routine"
```

Create a few harmless dummy commits on top:
```powershell
Add-Content -Path README.md -Value "<!-- note 1 -->"; git commit -am "docs: note 1"
Add-Content -Path README.md -Value "<!-- note 2 -->"; git commit -am "docs: note 2"
```

Verify tests currently fail:
```powershell
python -m unittest discover tests
```

**Expected Output:**
```text
FAIL: test_divide_valid (tests.test_calculator.TestCalculatorBasicOperations)
AssertionError: 12 != 5.0
```

---

#### Step 3: Run Automated Bisect
Start the bisect engine:
```powershell
git bisect start

# Tell Git that the current HEAD is broken
git bisect bad

# Tell Git a known historical commit that was good
git bisect good <your-initial-commit-hash>
```

Git automatically checks out the midpoint commit:
```text
Bisecting: 1 revision left to test after this (roughly 1 step)
```

Now let Git run the test suite automatically at each step:
```powershell
git bisect run python -m unittest tests/test_calculator.py
```

Git executes the test command at each step, automatically evaluating the exit code (`0` = good, non-zero = bad), until it isolates the exact culprit:

```text
...
a1b2c3d4e5f is the first bad commit
commit a1b2c3d4e5f
Author: ...
Date: ...

    refactor(calc): optimize division routine

 src/calculator.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
bisect found first bad commit
```

#### Step 4: Finish Bisect Session
Return to normal branch state:
```powershell
git bisect reset
```

Delete the simulation branch:
```powershell
git switch main
git branch -D bisect-simulation
```

---

## 🔍 Verification Steps
1. Run `git status` — confirm return to `main` with clean working tree.
2. Run `python -m unittest discover tests` — all unit tests pass with `OK`.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `git bisect` gets stuck | Test command didn't return standard exit codes (0 for success, non-zero for failure). | Use standard test runners like `python -m unittest` or `pytest`. |
| Forgetting to run `git bisect reset` | Repository remains in detached HEAD state. | Run `git bisect reset` to return to your original branch. |
| Inverting good and bad marks | Marking broken commit as good or vice versa. | Run `git bisect reset` and restart the bisect session with correct markers. |

---

## ✅ Completion Checklist
- [ ] Searched commit history using keyword grep (`git log --grep`).
- [ ] Tracked code additions across history with pickaxe (`git log -S`).
- [ ] Inspected line-by-line author attribution with `git blame`.
- [ ] Simulated a regression on a topic branch.
- [ ] Executed automated binary search debugging using `git bisect run`.
- [ ] Concluded bisect session with `git bisect reset`.
