# 🌿 Lab 03: Branching Lifecycle & Parallel Development

> **Objective**: Create, switch, list, and visualize independent branches; understand branch pointer mechanics in Git internals; and manage branch hygiene.

---

## 📋 Prerequisites
1. Completion of Lab 02.
2. Clean working tree (`git status` shows `nothing to commit, working tree clean`).
3. Understanding of commit hashes and the `.git/refs/heads/` directory.

---

## 📖 Theoretical Context: Branches are Just Lightweight Pointers

In Git, a branch is not a massive folder clone. It is a 41-byte text reference file storing the 40-character SHA hash of its head commit.

When you run:
```powershell
git switch -c feature/robot-telemetry
```
Git simply:
1. Writes the current commit SHA into `.git/refs/heads/feature/robot-telemetry`.
2. Updates `.git/HEAD` to point to `ref: refs/heads/feature/robot-telemetry`.

```
                  HEAD
                   │
                   ▼
       [feature/robot-telemetry Branch Pointer]
                   │
                   ▼
            [Commit b2c3d4e]
                   ▲
                   │
         [main Branch Pointer]
```

When you make a new commit on `feature/robot-telemetry`, only the `feature/robot-telemetry` pointer advances. `main` stays where it was!

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 3.1: Modern Branch Navigation
Git 2.23 introduced `git switch` to replace the overloaded `git checkout` command.

```powershell
# Create and jump to a new branch:
git switch -c feature/robot-telemetry

# Check your current branch:
git branch --show-current
```

**Expected Output:**
```text
feature/robot-telemetry
```

Inspect the hidden pointer inside `.git` using PowerShell:
```powershell
Get-Content .git/HEAD
```

**Expected Output:**
```text
ref: refs/heads/feature/robot-telemetry
```

---

### Task 3.2: Implement Telemetry Feature on Branch
Add a helper in `src/calculator.py` for computing Euclidean distance:

```python
def euclidean_distance(x1: Number, y1: Number, x2: Number, y2: Number) -> float:
    """Calculate 2D Euclidean distance between two coordinate points.

    Useful for waypoint navigation and obstacle clearance checking.

    Args:
        x1, y1: Coordinates of Point 1.
        x2, y2: Coordinates of Point 2.

    Returns:
        Straight-line distance as a float.
    """
    _validate_numeric(x1, "x1")
    _validate_numeric(y1, "y1")
    _validate_numeric(x2, "x2")
    _validate_numeric(y2, "y2")
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
```

Add corresponding test in `tests/test_calculator.py`:
```python
    def test_euclidean_distance(self):
        """Verify 2D Euclidean distance between coordinates."""
        from src.calculator import euclidean_distance
        self.assertEqual(euclidean_distance(0, 0, 3, 4), 5.0)
        self.assertEqual(euclidean_distance(1, 1, 1, 1), 0.0)
```

Test and commit:
```powershell
python -m unittest discover tests
git add src/calculator.py tests/test_calculator.py
git commit -m "feat(calc): implement 2D euclidean_distance for robot navigation"
```

---

### Task 3.3: Branch Switching & Working Tree Restoration
Switch back to `main`:
```powershell
git switch main
```

Now open `src/calculator.py`. Notice that `euclidean_distance` is **not present**! Git automatically swapped the working tree files to match the commit snapshot on `main`.

Switch back to the feature branch:
```powershell
git switch feature/robot-telemetry
```
`euclidean_distance` is immediately restored.

---

### Task 3.4: Visualizing History Graphs
Configure a custom Git alias for an ASCII tree graph:

```powershell
git config --global alias.tree "log --graph --oneline --decorate --all"
```

Now run:
```powershell
git tree
```

**Expected Output:**
```text
* 7a8b9c0 (HEAD -> feature/robot-telemetry) feat(calc): implement 2D euclidean_distance for robot navigation
* b2c3d4e (main) feat(calc): implement absolute_value and document in changelog
* 9d4e12a chore: initial repository setup with core modules, tests, and documentation
```

---

### Task 3.5: Branch Inspection & Safe Deletion Rules

```powershell
# List all local branches with their latest commit SHA and title
git branch -v

# Check which branches are merged into your current branch
git branch --merged

# Check which branches are unmerged
git branch --no-merged
```

If you try to delete `feature/robot-telemetry` while on `main`:
```powershell
git switch main
git branch -d feature/robot-telemetry
```

Git protects you from accidental data loss:
```text
error: The branch 'feature/robot-telemetry' is not fully merged.
If you are sure you want to delete it, run 'git branch -D feature/robot-telemetry'.
```

*(Leave `feature/robot-telemetry` intact; we will merge it in Lab 04).*

---

## 🔍 Verification Steps
1. Run `git branch` — confirm both `main` and `feature/robot-telemetry` are listed.
2. Run `git switch feature/robot-telemetry; python -m unittest discover tests` — all tests pass.
3. Run `git switch main; python -m unittest discover tests` — all tests pass.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `fatal: A branch named 'feature/...' already exists` | Attempted to create an existing branch with `-c`. | Switch to it using `git switch <branch-name>` without `-c`. |
| Uncommitted changes prevent switching branches | Working tree changes collide with incoming branch commits. | Commit changes, stash them (`git stash`), or discard them (`git restore .`). |
| Accidental branch deletion | Used uppercase `-D` instead of lowercase `-d`. | Find the lost commit SHA using `git reflog` and run `git switch -c <branch-name> <commit-sha>`. |

---

## ✅ Completion Checklist
- [ ] Created and switched to a feature branch using `git switch -c`.
- [ ] Verified branch pointer reference inside `.git/HEAD`.
- [ ] Implemented and committed a feature on the isolated branch.
- [ ] Verified working tree swap when switching back to `main`.
- [ ] Configured and tested the `git tree` visualization alias.
- [ ] Inspected merged vs unmerged branch states with `git branch --merged`.
