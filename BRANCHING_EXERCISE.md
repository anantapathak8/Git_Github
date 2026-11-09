# 🌿 Practical Branching Exercise: Isolation & Parallel Feature Development

> **Robotics & AI B.Tech Curriculum — Week 3 Lab**  
> **Target**: Master branch lifecycle, context switching, parallel tracking, and branch hygiene.

---

## 🎯 Objective
Learn how Git manages branches as lightweight movable pointers to commit hashes; master modern `git switch` commands; work simultaneously on two distinct feature branches without cross-contamination; visualize branch topology; and safely clean up merged branches.

---

## 📋 Prerequisites
1. Local Git repository initialized on `main` with initial commit.
2. Clean working tree (`git status` shows clean).
3. Test suite passing (`python -m unittest discover tests`).

---

## 🧠 Conceptual Foundation: How Git Branches Work

In many legacy version control systems, creating a branch requires copying the entire project directory tree. In Git, a branch is simply a **41-byte text file** located in `.git/refs/heads/<branch-name>` containing the 40-character SHA hash of its latest commit!

```
[Commit A] <--- [Commit B] <--- [Commit C] <=== main
                                      ^
                                      +====== feature/calc-modulo (HEAD)
```

Creating or switching branches is instantaneous (`O(1)` time complexity) regardless of repository size.

---

## 🛠 Step-by-Step Instructions & Exact Commands

### Step 1: Check Current Branch State
Before branching, verify your repository status and identify your active branch in PowerShell:

```powershell
git status
git branch -v
```

**Expected Output:**
```text
On branch main
nothing to commit, working tree clean
* main  9d4e12a chore: initial repository setup with core modules, tests, and documentation
```
*(The asterisk `*` designates your active branch where `HEAD` is pointing).*

---

### Step 2: Create and Switch to Feature Branch 1
Let's build an advanced mathematical function in `src/calculator.py` representing a robot telemetry modulus/remainder operation.

Modern syntax (Git 2.23+):
```powershell
git switch -c feature/calc-modulo
```

*(Legacy equivalent: `git checkout -b feature/calc-modulo`)*

Verify you are on the new branch:
```powershell
git branch
```

**Expected Output:**
```text
* feature/calc-modulo
  main
```

---

### Step 3: Implement Feature 1 on Its Branch
Open `src/calculator.py` and append the modulo operation:

```python
def modulo(a: Number, b: Number) -> Number:
    """Return the remainder of dividing a by b (a % b).

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        Remainder of division.

    Raises:
        TypeError: If operands are non-numeric.
        ZeroDivisionError: If b is 0.
    """
    _validate_numeric(a, "Operand 'a'")
    _validate_numeric(b, "Operand 'b'")
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is undefined.")
    return a % b
```

Next, open `tests/test_calculator.py` and append unit test verification:
```python
    def test_modulo_operation(self):
        """Verify remainder calculations."""
        from src.calculator import modulo
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)
```

Run test suite to verify:
```powershell
python -m unittest discover tests
```

Commit the new feature to your branch:
```powershell
git add src/calculator.py tests/test_calculator.py
git commit -m "feat(calc): implement modulo function with zero division validation"
```

---

### Step 4: Context Switch Back to `main`
Imagine an urgent requirement arises to add a new greeting mode before `feature/calc-modulo` is merged.

Switch back to `main`:
```powershell
git switch main
```

Inspect `src/calculator.py`! Notice that the `modulo` function is **completely absent** here. Your working directory cleanly reverted to the snapshot on `main`.

---

### Step 5: Create Feature Branch 2 Off `main`
Now, spawn another branch from `main`:

```powershell
git switch -c feature/cybernetic-greeting
```

Edit `src/greeting.py` to add a new `"cybernetic"` style option inside `greet()`:
```python
    if clean_style == "cybernetic":
        prefix = f"{clean_title} " if clean_title else ""
        return f"[CYBERNETIC CORE] Neural sync established with operator {prefix}{clean_name}."
```
*(Also add `'cybernetic'` to the set of valid styles in `_validate_style`).*

Add corresponding unit test in `tests/test_greeting.py`:
```python
    def test_cybernetic_greeting(self):
        """Verify cybernetic operator format."""
        result = greet("Anant", style="cybernetic")
        self.assertIn("Neural sync established", result)
```

Commit this feature:
```powershell
python -m unittest discover tests
git add src/greeting.py tests/test_greeting.py
git commit -m "feat(greeting): add cybernetic AI persona greeting format"
```

---

### Step 6: Visualize Branch Divergence
You now have two branches that have diverged from `main` in different directions! Run Git's graphical log viewer:

```powershell
git log --graph --oneline --all --decorate
```

**Expected Visualization:**
```text
* 4f3a1b2 (HEAD -> feature/cybernetic-greeting) feat(greeting): add cybernetic AI persona
| * a1b2c3d (feature/calc-modulo) feat(calc): implement modulo function
|/
* 9d4e12a (main) chore: initial repository setup with core modules, tests, and documentation
```

---

### Step 7: Merging Feature 1 (Fast-Forward Demonstration)
Switch back to `main` and integrate `feature/calc-modulo`:

```powershell
git switch main
git merge feature/calc-modulo
```

Because `main` had not moved forward since `feature/calc-modulo` was spawned, Git performs a **Fast-Forward (FF)** merge by simply advancing the `main` pointer forward!

**Expected Output:**
```text
Updating 9d4e12a..a1b2c3d
Fast-forward
 src/calculator.py         | 18 ++++++++++++++++++
 tests/test_calculator.py  |  8 ++++++++
 2 files changed, 26 insertions(+)
```

---

### Step 8: Merging Feature 2 (Three-Way Recursive Merge)
Now integrate `feature/cybernetic-greeting`:

```powershell
git merge feature/cybernetic-greeting -m "merge: integrate cybernetic greeting feature"
```

Because `main` has progressed with commit `a1b2c3d`, Git detects divergent commits and performs a **3-Way Merge** (`ORT` strategy).

Since Feature 1 touched `calculator.py` and Feature 2 touched `greeting.py`, Git combines them automatically with **zero conflicts**!

---

### Step 9: Cleaning Up Stale Branches
Once branches are merged into `main`, keeping them around creates clutter:

```powershell
# List all branches already merged into current branch
git branch --merged

# Safely delete local merged branches
git branch -d feature/calc-modulo
git branch -d feature/cybernetic-greeting
```

---

## 🔍 Verification Steps
1. Run `git branch` — confirm only `main` remains.
2. Run `python -m unittest discover tests` — all unit tests pass.
3. Run `git log --graph --oneline -n 6` — verify 3-way merge commit geometry.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| Cannot switch branches due to uncommitted edits | Working tree contains uncommitted changes. | Commit them, stash them (`git stash`), or discard with `git restore .`. |
| `git branch -d` fails with unmerged error | Attempted to delete a branch before merging. | Merge branch first, or use uppercase `-D` if intentionally abandoning work. |
| Merged wrong branch into `main` | Forgot to check active branch before merging. | Run `git reset --hard ORIG_HEAD` or `git reset --hard HEAD~1` to undo local merge. |

---

## ✅ Completion Checklist
- [ ] Created parallel branches `feature/calc-modulo` and `feature/cybernetic-greeting`.
- [ ] Switched between branches verifying working tree file swapping.
- [ ] Visualized branch divergence using `git log --graph`.
- [ ] Executed Fast-Forward merge on Feature 1.
- [ ] Executed 3-Way merge on Feature 2.
- [ ] Cleaned up stale merged branches with `git branch -d`.
