# 🚀 Lab 07: Pull Requests, Code Reviews & Collaboration Gates

> **Objective**: Create feature branches, push them to GitHub, open structured Pull Requests utilizing PR templates, participate in code reviews, handle suggestions, and execute safe merge strategies.

---

## 📋 Prerequisites
1. Completion of Lab 06 (local repository pushed and linked to GitHub).
2. GitHub CLI (`gh`) installed (optional, but recommended: `winget install GitHub.cli`).
3. Clean working tree on `main`.

---

## 📖 Theoretical Context: The GitHub Pull Request

A **Pull Request (PR)** is a GitHub platform primitive built on top of Git. It notifies maintainers and peers that a set of commits on a topic branch is ready for review and integration into the upstream repository.

PRs provide:
- **Code Review**: Interactive line-by-line discussions.
- **Automated CI/CD Gates**: Running unit tests (`python -m unittest discover tests`) before permission to merge.
- **Deployment Previews**: Ephemeral test environments.

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 7.1: Create a Feature Branch and Push
Let's add a robot velocity calculator to `src/calculator.py`:

```powershell
git switch main
git pull origin main
git switch -c feature/robot-kinematic-velocity
```

Add the function in `src/calculator.py`:
```python
def calculate_velocity(displacement: Number, time_elapsed: Number) -> float:
    """Calculate linear velocity (v = d / t) for autonomous rover navigation.

    Args:
        displacement: Distance traversed in meters.
        time_elapsed: Duration in seconds.

    Returns:
        Velocity in meters/second.

    Raises:
        ZeroDivisionError: If time_elapsed is zero.
        ValueError: If time_elapsed is negative.
    """
    _validate_numeric(displacement, "Displacement")
    _validate_numeric(time_elapsed, "Time elapsed")
    if time_elapsed == 0:
        raise ZeroDivisionError("Time elapsed cannot be zero.")
    if time_elapsed < 0:
        raise ValueError("Time elapsed must be non-negative.")
    return displacement / time_elapsed
```

Add corresponding test in `tests/test_calculator.py`:
```python
    def test_calculate_velocity(self):
        """Verify linear velocity calculation."""
        from src.calculator import calculate_velocity
        self.assertEqual(calculate_velocity(100, 10), 10.0)
        with self.assertRaises(ZeroDivisionError):
            calculate_velocity(100, 0)
        with self.assertRaises(ValueError):
            calculate_velocity(100, -5)
```

Run test suite:
```powershell
python -m unittest discover tests
```

Commit and push with upstream tracking:
```powershell
git add src/calculator.py tests/test_calculator.py
git commit -m "feat(calc): implement calculate_velocity with physical constraints"
git push -u origin feature/robot-kinematic-velocity
```

---

### Task 7.2: Opening a Pull Request

#### Option A: Via GitHub Web Interface
1. Go to your repository on `github.com`.
2. A banner appears: *"feature/robot-kinematic-velocity had recent pushes"*. Click **Compare & pull request**.
3. Notice that `.github/PULL_REQUEST_TEMPLATE.md` automatically populates the description box!
4. Fill in the template fields:
   - Check `[x] ✨ New feature`
   - Check `[x] 🧪 Tests added`
   - Fill in testing proof (`python -m unittest discover tests`).
5. Click **Create pull request**.

#### Option B: Via GitHub CLI (`gh`)
```powershell
gh pr create --title "feat(calc): add linear velocity calculation for rover navigation" --body-file .github/PULL_REQUEST_TEMPLATE.md
```

---

### Task 7.3: The Code Review Workflow

When reviewers examine your PR:

1. **Inline Suggestions**: Reviewers can propose exact code edits using GitHub's suggestion syntax:
   ````markdown
   ```suggestion
   if time_elapsed <= 0:
       raise ValueError("Time elapsed must be strictly positive (> 0).")
   ```
   ````
2. **Applying Suggestions**: The PR author can click **Commit suggestion** directly in GitHub's web interface! GitHub will author a commit directly onto the topic branch.
3. **Local Pull of Suggestions**: To pull review commits back into your local branch:
```powershell
git pull origin feature/robot-kinematic-velocity
```

---

### Task 7.4: Merging the Pull Request
Once approved and status checks pass:

Choose **Squash and merge**:
- Title: `feat(calc): implement calculate_velocity for rover navigation (#1)`
- Description: Automatically condenses the branch commits into a clean summary.
- Click **Confirm squash and merge**.

---

### Task 7.5: Post-Merge Local Cleanup
After merging and deleting the branch on GitHub:

```powershell
# Switch back to local main
git switch main

# Pull the freshly merged commit from GitHub
git pull origin main

# Delete the local feature branch
git branch -d feature/robot-kinematic-velocity

# Prune stale remote tracking references
git remote prune origin
```

Verify your local repository matches GitHub:
```powershell
git status
```

**Expected Output:**
```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

---

## 🔍 Verification Steps
1. Run `git branch -a` — verify no orphaned branch references remain.
2. Run `python -m unittest discover tests` — ensure the new velocity function is active and passing on `main`.
3. Check GitHub repository commit history — verify the single squashed commit appears cleanly on `main`.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| PR description is blank | PR template file was in wrong path. | Ensure template is located at `.github/PULL_REQUEST_TEMPLATE.md`. |
| PR cannot be merged automatically | Base branch on remote has diverged. | Run `git switch feature/...`, `git pull origin main`, resolve conflicts locally, and push. |
| Forgetting to delete merged branches | Accumulating dozens of stale branches. | Run `git branch -d <branch>` locally and click "Delete branch" on GitHub. |

---

## ✅ Completion Checklist
- [ ] Created and pushed a feature branch to GitHub.
- [ ] Opened a Pull Request utilizing `.github/PULL_REQUEST_TEMPLATE.md`.
- [ ] Practiced reviewing code diffs and handling suggestion commits.
- [ ] Merged PR using Squash and Merge strategy.
- [ ] Cleaned up local and remote feature branches.
