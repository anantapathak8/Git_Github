# Git & GitHub: Version Control, Collaboration and Professional Development Workflow

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Git 2.23+](https://img.shields.io/badge/git-2.23+-orange.svg)](https://git-scm.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Unit Tests](https://img.shields.io/badge/tests-31%20passed-brightgreen.svg)](tests/)
[![Curriculum](https://img.shields.io/badge/Curriculum-Week%203%20of%204-purple.svg)](#-academic-context--author-notes)

> **Portfolio Project — Week 3 of Four-Week Python Learning Roadmap**  
> **Student Specialization**: B.Tech in Robotics & Artificial Intelligence (3rd Year)  
> **Core Focus**: Industrial Git mechanics, branch workflows, conflict resolution, GitHub PR review gates, automated forensics, and collaborative software engineering.

---

## Table of Contents
1. [Project Overview & Learning Objectives](#-project-overview--learning-objectives)
2. [Key Competencies & Skills Acquired](#-key-competencies--skills-acquired)
3. [Repository Architecture](#-repository-architecture)
4. [Suggested Learning Sequence](#-suggested-learning-sequence)
5. [The 12 Practical Challenges](#-the-12-practical-challenges)
6. [Python Demonstration Modules](#-python-demonstration-modules)
   - [Calculator Module (`src/calculator.py`)](#calculator-module)
   - [Greeting Module (`src/greeting.py`)](#greeting-module)
7. [Automated Unit Testing Suite](#-automated-unit-testing-suite)
8. [Engineering Documentation Index](#-engineering-documentation-index)
9. [Git Quick Reference & Command Cheat Sheet](#-git-quick-reference--command-cheat-sheet)
10. [Academic Context & Author Notes](#-academic-context--author-notes)

---

## Project Overview & Learning Objectives

In advanced robotics stacks (such as ROS2 navigation, PX4 autopilot, SLAM nodes) and applied artificial intelligence pipelines (e.g., PyTorch vision models, inference agents), software engineering reliability is paramount. Distributed engineering teams cannot afford broken main branches, lost commits, or unreviewed code changes.

This repository serves as a **portfolio-grade engineering laboratory**. It couples an active, modular Python codebase with rigorous documentation, GitHub issue/PR templates, CI automation, and a **12-module progressive practice curriculum** that guides engineers from raw repository initialization to automated regression hunting (`git bisect`), interactive rebasing, and client-side pre-commit quality gates.

### Primary Learning Objectives:
- **Master Git Internals**: Understand object databases (`.git/objects`), commit DAGs, tree references, and the staging index.
- **Isolate Feature Tracks**: Apply Git Flow and GitHub Flow branching taxonomies using modern `git switch` workflows.
- **Demystify Conflicts**: Reproduce, diagnose, and resolve merge conflicts in terminal and visual merge editors with test verification.
- **Enforce Collaboration Gates**: Author PRs with Conventional Commits, review inline code suggestions, and maintain upstream synchronization.
- **Execute Disaster Recovery**: Recover uncommitted changes, invert public commits safely with `git revert`, and resurrect deleted commits with `git reflog`.
- **Automate Quality Assurance**: Employ client-side `pre-commit` hooks and GitHub Actions CI matrices running unit tests on Python 3.8 through 3.12.

---

## Key Competencies & Skills Acquired

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CORE COMPETENCIES & MATRIX                                    │
├────────────────────────────┬────────────────────────────┬────────────────────────────────────────┤
│  Git Internals & Staging   │  Branching & Integration   │  Disaster Recovery & Forensics         │
├────────────────────────────┼────────────────────────────┼────────────────────────────────────────┤
│ • Index vs Working Tree    │ • Fast-Forward & 3-Way     │ • git restore / git reset (--soft/hard)│
│ • Object database (.git)   │ • Merge conflict diagnosis │ • git revert (safe public undo)        │
│ • Conventional Commits     │ • Git Flow & GitHub Flow   │ • git stash task shelving              │
│ • Interactive patch mode   │ • Rebase vs Merge tradeoff │ • git reflog resurrection              │
│ • Commit amending          │ • Remote tracking branches │ • git bisect binary search hunt        │
│ • Client-side git hooks    │ • Upstream sync (--rebase) │ • Line attribution via git blame       │
└────────────────────────────┴────────────────────────────┴────────────────────────────────────────┘
```

---

## Repository Architecture

```text
Git_GitHub_Week03/
│
├── README.md                          # Comprehensive portfolio documentation & roadmap
├── GIT_WORKFLOW.md                    # Git architectures, branching models & Conventional Commits
├── GIT_CHEATSHEET.md                  # Comprehensive terminal command quick reference card
├── BRANCHING_EXERCISE.md              # Parallel feature branch simulation & lifecycle guide
├── MERGE_CONFLICT_GUIDE.md            # Deep dive on conflict markers, diagnosis & resolution
├── PULL_REQUEST_GUIDE.md              # Professional PR lifecycle, reviews, suggestions & CLI
├── CONTRIBUTING.md                    # Open-source developer standards & PEP 8 guidelines
├── CHANGELOG.md                       # Semantic versioning release log (Keep a Changelog format)
├── LICENSE                            # MIT Open Source License
├── requirements-dev.txt               # Development & linting tooling dependencies
├── .gitignore                         # Python, IDE, OS, and sandbox exclusion rules
│
├── src/                               # Production Demonstration Codebase
│   ├── calculator.py                  # Modular arithmetic, robotics telemetry, and validation
│   └── greeting.py                    # Configurable greetings, time-aware formatting, and banners
│
├── tests/                             # Built-in Unittest Test Suite
│   ├── test_calculator.py             # 17 unit tests covering arithmetic, floats & zero-division
│   └── test_greeting.py               # 14 unit tests validating styles, hours & error handling
│
├── practice_lab/                      # 12-Module Hands-On Engineering Curriculum
│   ├── README.md                      # Lab roadmap, objectives, and prerequisites
│   ├── 01_repository_setup.md         # Lab 1: Identity, init, .git internals & .gitignore
│   ├── 02_commit_mastery.md           # Lab 2: Staging index, diffs, patch mode & amend
│   ├── 03_branching.md                # Lab 3: Modern branching, pointers & topology
│   ├── 04_merging_and_conflicts.md    # Lab 4: Fast-forward vs 3-way & conflict solving
│   ├── 05_undo_and_recovery.md        # Lab 5: Restore, reset trio, revert, stash & reflog
│   ├── 06_remote_operations.md        # Lab 6: Remotes, push -u, fetch vs pull, SSH/PAT
│   ├── 07_pull_requests.md            # Lab 7: PR lifecycle, templates, review suggestions
│   ├── 08_collaboration_simulation.md # Lab 8: Multi-engineer local simulation (Alice & Bob)
│   ├── 09_history_investigation.md    # Lab 9: git blame, pickaxe & automated bisect
│   ├── 10_tags_and_releases.md        # Lab 10: SemVer, annotated tags & GitHub releases
│   ├── 11_rebasing_and_cherry_pick.md # Lab 11: Linear history, interactive rebase & cherry-pick
│   ├── 12_git_hooks_and_automation.md # Lab 12: Client-side pre-commit test quality gates
│   └── CHALLENGE_CHECKLIST.md         # 36-item practical mastery evaluation checklist
│
└── .github/                           # GitHub Collaboration & CI/CD Pipelines
    ├── PULL_REQUEST_TEMPLATE.md       # Standardized PR checklist and description schema
    ├── workflows/
    │   └── ci.yml                     # GitHub Actions CI matrix running tests on Python 3.8-3.12
    └── ISSUE_TEMPLATE/
        ├── bug_report.md              # Form for reporting defects with system details
        └── feature_request.md         # Structured feature proposal form for robotics/AI utilities
```

---

## Suggested Learning Sequence

For optimal mastery, follow this 7-day progression during Week 3:

```
[Day 1: Foundations]   --> [Day 2: Staging & Branches] --> [Day 3: Merges & Conflicts]
  - Read GIT_WORKFLOW        - Lab 02 (Commit Mastery)       - Lab 04 (Merging & Conflicts)
  - Lab 01 (Repo Setup)      - Lab 03 (Branching)            - MERGE_CONFLICT_GUIDE.md
                                                             - BRANCHING_EXERCISE.md

[Day 4: Safety & Recovery]--> [Day 5: GitHub & Collab]   --> [Day 6: Forensics & Releases] --> [Day 7: Review]
  - Lab 05 (Undo & Reflog)   - Lab 06 (Remote Ops)           - Lab 09 (Bisect & Blame)        - CHALLENGE_CHECKLIST
                             - Lab 07 (Pull Requests)        - Lab 10 (Tags & Releases)       - Run full test suite
                             - Lab 08 (Alice & Bob Collab)   - Lab 11 (Rebase & Cherry-pick)  - Portfolio sign-off
                                                             - Lab 12 (Pre-Commit Hooks)
```

---

## The 12 Practical Challenges

Every challenge module in `practice_lab/` is equipped with **Objectives, Prerequisites, Step-by-Step Instructions, Exact PowerShell Commands, Expected Outputs, Verification Steps, Common Mistakes & Solutions, and Completion Checklists**:

| Module | Title | Core Focus | Link |
| :---: | :--- | :--- | :---: |
| **01** | **Repository Setup** | Identity configuration, `git init`, `.git` directory anatomy, and `.gitignore` verification. | [Lab 01](practice_lab/01_repository_setup.md) |
| **02** | **Commit Mastery** | Staging index mechanics, `git diff` vs `git diff --staged`, patch staging (`-p`), and `git commit --amend`. | [Lab 02](practice_lab/02_commit_mastery.md) |
| **03** | **Branching Lifecycle** | Pointer theory, modern `git switch -c`, topology visualization, and branch hygiene. | [Lab 03](practice_lab/03_branching.md) |
| **04** | **Merging & Conflicts** | Fast-forward merges, 3-way ORT strategy, intentionally generating collisions, and CLI resolution. | [Lab 04](practice_lab/04_merging_and_conflicts.md) |
| **05** | **Undo & Recovery** | `git restore`, soft/mixed/hard `git reset`, safe public `git revert`, `git stash`, and `git reflog` resurrection. | [Lab 05](practice_lab/05_undo_and_recovery.md) |
| **06** | **Remote Operations** | Remote configuration, upstream tracking (`-u`), `git fetch` vs `git pull`, and authentication. | [Lab 06](practice_lab/06_remote_operations.md) |
| **07** | **Pull Requests** | GitHub PR lifecycle, automated templates, inline code review suggestions, and merge modes. | [Lab 07](practice_lab/07_pull_requests.md) |
| **08** | **Collaboration Simulation** | Simulating a multi-developer team (Alice & Bob) locally to experience concurrent push rejections and rebase workflows. | [Lab 08](practice_lab/08_collaboration_simulation.md) |
| **09** | **History Forensics** | `git blame`, pickaxe searching (`-S`), and automated binary regression testing using `git bisect run`. | [Lab 09](practice_lab/09_history_investigation.md) |
| **10** | **Tags & Releases** | SemVer 2.0.0, annotated release tags (`git tag -a`), tag synchronization, and GitHub Releases. | [Lab 10](practice_lab/10_tags_and_releases.md) |
| **11** | **Rebasing & Cherry-Pick**| Interactive rebase (`git rebase -i`), squashing interim commits, and surgical commit cherry-picking. | [Lab 11](practice_lab/11_rebasing_and_cherry_pick.md) |
| **12** | **Git Hooks & Automation** | Client-side `.git/hooks/pre-commit` test verification to block broken commits automatically. | [Lab 12](practice_lab/12_git_hooks_and_automation.md) |

Track your progress across all challenges using the **[36-Challenge Verification Checklist](practice_lab/CHALLENGE_CHECKLIST.md)**.

---

## Python Demonstration Modules

The codebase under `src/` provides clean, tested demonstration utilities designed to be modified during Git branching, merging, and conflict exercises.

### Calculator Module (`src/calculator.py`)
Features strict type validation (disallowing non-numerics and booleans) and domain utilities:
- `add(a, b)`: Arithmetic summation.
- `subtract(a, b)`: Difference calculation.
- `multiply(a, b)`: Scaling product.
- `divide(a, b)`: Float division with explicit `ZeroDivisionError` handling.
- `power(base, exponent)`: Exponential power using `math.pow`.
- `square_root(x)`: Square root with negative-value `ValueError` check.
- `calculate_mean(values)`: Sequence averaging for robotic sensor smoothing.

**Direct Execution:**
```powershell
python src/calculator.py
```

### Greeting Module (`src/greeting.py`)
Demonstrates string manipulation, sanitization, and configurable formatting:
- `greet(name, style, title)`: Styles include `standard`, `formal`, `casual`, `robotics` (telemetry active mode), and `developer` (debug session format).
- `get_time_based_greeting(name, current_hour)`: Time-aware greetings (Morning, Afternoon, Evening, Night Owl).
- `format_multiline_banner(name, project_name)`: Formatted CLI banner for robot operators.

**Direct Execution:**
```powershell
python src/greeting.py
```

---

## Automated Unit Testing Suite

The project utilizes Python's built-in `unittest` framework with zero external dependencies.

### Running All Tests:
```powershell
python -m unittest discover tests
```

**Expected Output:**
```text
Ran 31 tests in 0.001s

OK
```

### Running Individual Test Suites:
```powershell
python tests/test_calculator.py
python tests/test_greeting.py
```

---

## Engineering Documentation Index

- **[GIT_WORKFLOW.md](GIT_WORKFLOW.md)**: Deep dive into Git Flow, GitHub Flow, Trunk-Based Development, branch taxonomy, and Conventional Commits.
- **[GIT_CHEATSHEET.md](GIT_CHEATSHEET.md)**: Comprehensive command quick reference card.
- **[BRANCHING_EXERCISE.md](BRANCHING_EXERCISE.md)**: Step-by-step parallel feature branch simulation.
- **[MERGE_CONFLICT_GUIDE.md](MERGE_CONFLICT_GUIDE.md)**: Comprehensive guide on conflict marker anatomy and resolution strategies.
- **[PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md)**: Standards for creating, reviewing, and merging high-impact PRs.
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Contributor standards, PEP 8 compliance, and issue workflow.
- **[CHANGELOG.md](CHANGELOG.md)**: Structured project evolution following Keep a Changelog.

---

## Git Quick Reference & Command Cheat Sheet

```powershell
# === INITIALIZATION & CONFIGURATION ===
git init                                      # Initialize a local Git repository
git config --global user.name "Your Name"     # Set global author name
git config --global user.email "you@lab.edu"  # Set global author email
git config --global init.defaultBranch main    # Set default branch name to main

# === STAGING & COMMITTING ===
git status                                    # Inspect working directory & staging index
git diff                                      # Diff between working directory and staging index
git diff --staged                             # Diff between staging index and HEAD commit
git add <file>                                # Stage specific file
git add -p                                    # Interactively stage hunks of code
git commit -m "type(scope): description"      # Commit staged changes with semantic message
git commit --amend                            # Modify the most recent commit

# === BRANCHING & MERGING ===
git branch -v                                 # List local branches with latest commit
git switch -c <branch>                        # Create and jump to a new branch
git switch <branch>                           # Switch to an existing branch
git merge <branch>                            # Merge branch into currently checked-out branch
git merge --abort                             # Abort an active merge conflict cleanly
git branch -d <branch>                        # Safely delete a merged branch

# === UNDO & DISASTER RECOVERY ===
git restore <file>                            # Discard unstaged changes in working tree
git restore --staged <file>                   # Unstage file back to working tree
git reset --soft HEAD~1                       # Undo commit, keep changes staged
git reset --mixed HEAD~1                      # Undo commit, keep changes unstaged
git reset --hard HEAD~1                       # Undo commit and wipe changes (destructive!)
git revert <commit>                           # Create a new commit that inverts specified commit
git stash save "message"                      # Shelve uncommitted changes
git stash pop                                 # Restore most recently shelved changes
git reflog                                    # View complete local history of HEAD movements

# === REMOTE & COLLABORATION ===
git remote add origin <url>                   # Bind local repository to remote GitHub URL
git push -u origin main                       # Push branch and configure upstream tracking
git fetch origin                              # Download remote commits without modifying working tree
git pull --rebase origin main                 # Fetch and reapply local commits on top of remote main
git tag -a v1.0.0 -m "Release v1.0.0"         # Create annotated release tag
git push origin --tags                        # Push all local tags to GitHub
```

---

## Academic Context & Author Notes

This project is **Week 3** of a structured 4-week Python and Software Engineering learning program:

- **Week 1:** Python Fundamentals, Data Structures & Algorithmic Foundations
- **Week 2:** Object-Oriented Programming (OOP), Modules, Exception Handling & File Management
- **Week 3:** **Git, GitHub, Version Control, Collaboration & Professional Engineering Practices** *(This Project)*
- **Week 4:** Capstone Project — Building a Python-based CLI Expense Tracker with JSON Persistence, Testing & Documentation

**Author:** B.Tech Computer Science Engineering Student, specializing in Robotics & Artificial Intelligence  
**Academic Focus:** Software Development, Robotics, Artificial Intelligence & Cybersecurity  
**License:** MIT License — Open for academic learning, reference and collaboration.
