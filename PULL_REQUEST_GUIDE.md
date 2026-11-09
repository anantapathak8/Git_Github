# 🚀 Professional Pull Request (PR) Guide: Code Review & Collaboration

> **Robotics & AI B.Tech Curriculum — Week 3 Lab**  
> *"A Pull Request is not merely a request to merge code; it is a collaborative peer-review discussion, a historical design document, and an automated verification gateway."*

---

## 📑 Table of Contents
1. [The Philosophy of Great Pull Requests](#1-the-philosophy-of-great-pull-requests)
2. [Anatomy of an Exemplary Pull Request](#2-anatomy-of-an-exemplary-pull-request)
3. [The End-to-End PR Lifecycle](#3-the-end-to-end-pr-lifecycle)
4. [Conducting and Receiving Code Reviews](#4-conducting-and-receiving-code-reviews)
5. [Keeping PRs In-Sync with Upstream](#5-keeping-prs-in-sync-with-upstream)
6. [Merge Strategies Compared: Merge Commit vs Squash vs Rebase](#6-merge-strategies-compared)
7. [Automating PR Workflows with GitHub CLI (`gh`)](#7-automating-pr-workflows-with-github-cli-gh)

---

## 1. The Philosophy of Great Pull Requests

In top-tier engineering organizations (NASA JPL, Boston Dynamics, Google DeepMind), code cannot reach production without peer scrutiny. Pull Requests ensure:
- **Code Quality & Reliability**: Bugs, edge-case oversights, and race conditions are caught before deployment.
- **Shared Team Knowledge**: No individual is an isolated silo; team members learn from each other's design choices.
- **Architectural Documentation**: The PR discussion thread preserves the *why* behind algorithmic decisions for future engineers.

---

## 2. Anatomy of an Exemplary Pull Request

A low-effort PR description like *"Fixed bug"* or *"Updated calculator"* wastes reviewer time and causes delays. An exemplary PR contains structured context:

```markdown
## 📌 Description
Adds Euclidean distance and angle calculation utilities to `src/calculator.py`
for 2D LiDAR coordinate navigation.

Closes #14

## 🛠 Type of Change
- [x] ✨ New feature
- [ ] 🐛 Bug fix
- [x] 🧪 Tests added

## 🧪 Testing Verification
- Added 12 unit tests in `tests/test_calculator.py` covering positive, negative, and collinear points.
- Executed `python -m unittest discover tests` with 100% pass rate.
- Benchmark: 100,000 coordinate transforms evaluated in < 40ms.

## 📸 Demonstration
```
Input: Point A (0, 0), Point B (3, 4)
Output: Distance = 5.0, Angle = 0.927 rad (53.13 deg)
```

## 📋 Pre-Merge Checklist
- [x] Conforms to PEP 8
- [x] Docstrings adhere to Google Python style guide
- [x] PR Template checklist fulfilled
```

---

## 3. The End-to-End PR Lifecycle

```
[Local Feature Branch]
        │
        ▼ git push -u origin feature/branch
[Remote Feature Branch on GitHub]
        │
        ▼ Click "Open Pull Request"
[Pull Request Discussion Opened]
   ├── Automated CI Status Checks (Unit Tests, Linter, Type Checker)
   ├── Peer Code Review (Comments, Suggestions)
   └── Iterative Commits addressing review feedback
        │
        ▼ Approved by Reviewers
[Merged into Main Branch]
        │
        ▼ Branch Deleted
[Local Cleanup: git branch -d feature/branch]
```

### Detailed Commands:
```bash
# 1. Update local main and create topic branch
git checkout main
git pull origin main
git checkout -b feature/robotic-pose-calc

# 2. Develop feature, add tests, verify
python -m unittest discover tests

# 3. Stage and commit atomically
git add src/calculator.py tests/test_calculator.py
git commit -m "feat(calc): implement 2D pose difference calculation"

# 4. Push to remote fork/origin
git push -u origin feature/robotic-pose-calc
```

Once pushed, GitHub outputs a direct terminal link to open the PR.

---

## 4. Conducting and Receiving Code Reviews

### For Reviewers: Constructive Code Review Mindset
- **Review with Empathy**: Critique the code, never the author.
- **Explain the Rationale**: Rather than stating *"Change this loop"*, explain *"Using list comprehension here reduces execution overhead during 50Hz sensor polling"*.
- **Categorize Feedback Severity**:
  - `[BLOCKER]`: Critical bug, security flaw, or failing test that must be fixed before merge.
  - `[SUGGESTION]`: Recommended improvement or cleaner idiom. Non-blocking.
  - `[NITPICK]`: Minor styling or cosmetic preference. Explicitly non-blocking.
  - `[QUESTION]`: Inquiring about design intent to deepen understanding.

### For Authors: Responding to Feedback
- Acknowledge feedback with gratitude.
- Commit fixes directly to your feature branch and push—GitHub automatically refreshes the open PR!
- Mark resolved comment threads as **"Resolved"** once addressed.

---

## 5. Keeping PRs In-Sync with Upstream

While your PR is awaiting review, other team members will merge their work into `main`. To prevent drift and ensure clean integration:

### Method A: Rebase Onto Main (Linear, Clean History)
```bash
git checkout feature/robotic-pose-calc
git fetch origin
git rebase origin/main

# If conflicts occur, resolve them, git add, and:
# git rebase --continue

# Force-push with lease (safe force push)
git push --force-with-lease origin feature/robotic-pose-calc
```

> ⚠️ **Notice `--force-with-lease`**: Standard `git push -f` can overwrite teammate commits on the remote branch. `--force-with-lease` guarantees push will fail if someone else pushed commits to the remote branch while you were rebasing!

### Method B: Merge Main Into Feature Branch (Preserves Exact Lineage)
```bash
git checkout feature/robotic-pose-calc
git fetch origin
git merge origin/main
git push origin feature/robotic-pose-calc
```

---

## 6. Merge Strategies Compared

When clicking the green merge button on GitHub, three options appear:

| Option | What Git Does | When to Choose |
| :--- | :--- | :--- |
| **Create a merge commit** (`--no-ff`) | Retains every single feature branch commit and appends an explicit 2-parent merge commit on `main`. | Major architectural feature releases or long-running audit trails. |
| **Squash and merge** | Compresses all 15 commits on the branch into a single clean commit on `main`. | Daily feature tasks where interim commits are messy ("WIP", "fix typo"). |
| **Rebase and merge** | Fast-forwards commits from the branch onto `main` one-by-one without a merge commit. | Teams demanding a strictly linear 1-dimensional commit history. |

*Industry Standard Recommendation*: **Squash and Merge** for standard feature PRs ensures `main` commit logs remain readable, modular, and easy to revert.

---

## 7. Automating PR Workflows with GitHub CLI (`gh`)

Engineers often manage PRs directly from the terminal without leaving their code editor using GitHub's official CLI:

```bash
# Authenticate GitHub CLI
gh auth login

# Create a Pull Request interactively with pre-filled title and template
gh pr create --web

# View active PR status in terminal
gh pr status

# Check out a colleague's PR locally to run tests
gh pr checkout 42

# Approve and merge directly from terminal
gh pr review --approve -b "LGTM! Verified unit tests pass locally on Python 3.11."
gh pr merge --squash --delete-branch
```

