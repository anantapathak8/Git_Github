# 🌐 Git Workflow: Professional Engineering Standards

> **Author**: Robotics & Artificial Intelligence Engineering Curriculum (Week 3)  
> **Topic**: Version Control Architectures, Branching Strategies, and Release Lifecycles

---

## 📑 Table of Contents
1. [Introduction to Version Control](#1-introduction-to-version-control)
2. [The Three (and Four) Trees of Git](#2-the-three-and-four-trees-of-git)
3. [Branching Models in Industry](#3-branching-models-in-industry)
   - [Git Flow](#git-flow)
   - [GitHub Flow](#github-flow)
   - [Trunk-Based Development](#trunk-based-development)
4. [Branch Naming Taxonomies](#4-branch-naming-taxonomies)
5. [The Conventional Commits Standard](#5-the-conventional-commits-standard)
6. [Daily Feature Development Lifecycle](#6-daily-feature-development-lifecycle)
7. [Merge vs Rebase: Principles and Tradeoffs](#7-merge-vs-rebase-principles-and-tradeoffs)
8. [The Golden Rules of Collaborative Git](#8-the-golden-rules-of-collaborative-git)

---

## 1. Introduction to Version Control

In modern software development—particularly within multidisciplinary engineering fields such as **Robotics and Artificial Intelligence**—software rarely lives in isolation. Autonomous navigation stacks, sensor calibration pipelines, computer vision models, and low-level motor microcontrollers undergo continuous iteration across multidisciplinary teams.

A **Distributed Version Control System (DVCS)** like **Git** provides:
- **Immutable Historical Lineage**: Every snapshot (commit) is cryptographically signed with a SHA-1/SHA-256 hash.
- **Independent Experimentation**: High-risk algorithms (e.g., experimental SLAM or neural network pruning) can be developed on isolated branches without disrupting production stability.
- **Distributed Resilience**: Every developer’s machine possesses a complete, standalone mirror of the repository and its entire history.
- **Traceability & Accountability**: Clear accountability of who modified what line of code, when, and for what purpose.

---

## 2. The Three (and Four) Trees of Git

Understanding Git requires understanding its underlying architectural zones rather than treating commands as black-box incantations.

```
+-------------------+      git add       +-------------------+     git commit     +-------------------+
| Working Directory | -----------------> |   Staging Area    | -----------------> | Local Repository  |
| (Modified Files)  |                    |      (Index)      |                    |     (HEAD/DB)     |
+-------------------+ <----------------- +-------------------+                    +-------------------+
         |             git restore/reset           |                                        |
         |                                         |                                        | git push
         +-----------------------------------------+----------------------------------------+
                                                   |
                                                   v
                                      +--------------------------+
                                      |    Remote Repository     |
                                      |     (GitHub/GitLab)      |
                                      +--------------------------+
```

1. **Working Directory (Working Tree)**: The physical sandbox on your local file system where you edit code, run tests, and create files. Files here are untracked or modified.
2. **Staging Area (The Index)**: A binary cache file (`.git/index`) acting as a pre-commit inspection buffer. It decouples your temporary edits from what is packaged into the next permanent snapshot.
3. **Local Repository (Object Database)**: The permanent history stored inside `.git/objects/`. When you execute `git commit`, Git constructs a commit object pointing to a tree object containing snapshots of staged files.
4. **Remote Repository**: The central server (e.g., GitHub) used to synchronize and aggregate commits across a distributed team.

---

## 3. Branching Models in Industry

Choosing a branching model depends on team size, release frequency, and deployment requirements.

### Git Flow
Created by Vincent Driessen in 2010. It uses dual long-lived branches (`main` and `develop`) alongside temporary supporting branches:

```
main       ●======================================● (v1.0.0 Tagged Release)
           ^                                      ^
           | release/v1.0.0                       | hotfix/patch-1
develop    ●-----------●-------------●------------●
                       \            /
            feature/calc\----------/
```

- **`main`**: Production-ready code only.
- **`develop`**: Integration branch for upcoming features.
- **`feature/*`**: Branched off `develop`, merged back into `develop`.
- **`release/*`**: Prepares a release candidate; handles documentation, version bumps, and final bugfixes.
- **`hotfix/*`**: Branched directly from `main` to address critical production incidents immediately.

*Ideal For*: Scheduled releases, embedded software, hardware-dependent firmware, ROS robot distributions.

---

### GitHub Flow
A lightweight, modern workflow favored by web services, SaaS, and continuous deployment environments.

```
main      ●-------●--------------------●========● (Automated Deployment)
                   \                  /
    feature/branch  ●-------●--------● (Pull Request & Code Review)
```

1. Any branch off `main` is a feature branch.
2. Branch names are descriptive (e.g., `fix-nav-drift`).
3. Commit frequently and open a Pull Request early for feedback.
4. Once reviewed and CI tests pass, merge directly into `main` and deploy immediately.

*Ideal For*: Fast-paced projects, cloud APIs, microservices, research experiments.

---

### Trunk-Based Development
Practiced by high-performing engineering teams (Google, Meta, Netflix).

- Developers merge small, frequent batches into a single branch (`trunk` or `main`) multiple times a day.
- Relies heavily on **Feature Flags** (toggles) to hide uncompleted features in production.
- Prevents long-lived branch drift and catastrophic "merge hell".

---

## 4. Branch Naming Taxonomies

Consistent branch naming enables automated CI/CD filtering and team readability. Use lowercase, hyphen-separated tokens prefixed with a category identifier:

| Prefix | Usage / Scope | Example |
| :--- | :--- | :--- |
| `feature/` or `feat/` | New functionality or capabilities | `feature/kalman-filter` |
| `bugfix/` or `fix/` | Resolving an identified defect | `fix/zero-division-exception` |
| `hotfix/` | Critical production patch bypassing normal cycles | `hotfix/lidar-buffer-overflow` |
| `refactor/` | Code restructuring without behavioral change | `refactor/calculator-type-hints` |
| `docs/` | Pure documentation or diagram enhancements | `docs/update-architecture-diagram` |
| `test/` | Adding, fixing, or optimizing unit test suites | `test/add-greeting-edge-cases` |
| `chore/` | Tooling, dependency, or configuration updates | `chore/update-python-linter-rules` |

---

## 5. The Conventional Commits Standard

High-quality Git history tells a coherent story. Follow the **[Conventional Commits 1.0.0](https://www.conventionalcommits.org/)** specification:

```
<type>[optional scope]: <description>

[optional body explaining WHY, not WHAT]

[optional footer(s): Breaking changes, Issue references]
```

### Commit Types:
- `feat`: A new feature for the user or downstream consumer.
- `fix`: A bug fix.
- `docs`: Documentation-only changes.
- `style`: Formatting, missing semi-colons, whitespace (no code change).
- `refactor`: Refactoring production code without fixing a bug or adding a feature.
- `perf`: Performance improvements.
- `test`: Adding missing tests or correcting existing tests.
- `chore`: Build scripts, dependencies, or auxiliary tool modifications.

### High-Quality Example:
```
feat(calculator): implement arithmetic mean for telemetry stream

Add calculate_mean function to src/calculator.py to allow robotics
sensor buffers to be filtered prior to state estimation. Includes strict
numeric validation and empty-list protection.

Closes #42
```

---

## 6. Daily Feature Development Lifecycle

Here is the standard step-by-step terminal routine:

```bash
# 1. Ensure you have the latest updates from production
git checkout main
git pull origin main

# 2. Spawn an isolated topic branch
git checkout -b feature/robotic-distance-metrics

# 3. Perform atomic edits and run test suite
python -m unittest discover tests

# 4. Inspect your exact changes
git status
git diff

# 5. Stage specific files (avoid `git add .` indiscriminately)
git add src/calculator.py tests/test_calculator.py

# 6. Commit with semantic message
git commit -m "feat(calc): add euclidean distance function with 2D coordinate validation"

# 7. Push feature branch to remote
git push -u origin feature/robotic-distance-metrics

# 8. Open a Pull Request on GitHub for peer review and automated CI validation
```

---

## 7. Merge vs Rebase: Principles and Tradeoffs

When integrating changes from a feature branch back into main, developers can choose between **Merge** and **Rebase**.

| Dimension | `git merge` | `git rebase` |
| :--- | :--- | :--- |
| **History Shape** | Non-linear; preserves parallel branch topology with a merge commit. | Completely linear; re-applies commits sequentially on top of the base. |
| **Context Retention**| Preserves exact historical timeline and author timestamp. | Rewrites commit hashes; creates new commits with new SHA IDs. |
| **Reversibility** | Easy to undo an entire feature integration (`git revert -m 1 <hash>`). | Difficult to isolate a feature once rebased onto trunk. |
| **Best Practice** | Best for integrating finished PRs or long-lived public branches. | Best for keeping local feature branches updated against `origin/main`. |

### The Golden Rule of Rebasing:
> ⚠️ **NEVER rebase commits that have been pushed to a public, shared branch!**  
> Rebasing rewrites history. If teammates have based their work on existing commit hashes, rewriting those hashes forces painful merge reconciliation for everyone on the team.

---

## 8. The Golden Rules of Collaborative Git

1. **Commit Early, Commit Often, Commit Small**: Keep commits atomic. A commit should address a single logical concept so it can be cherry-picked or reverted without collateral damage.
2. **Never Commit Secrets or Artifacts**: Credentials, API keys, compiled binaries, `.env` files, and virtual environment folders (`.venv/`) must remain excluded via `.gitignore`.
3. **Always Run Tests Before Committing**: Never push broken code to a remote branch. Ensure `python -m unittest discover tests` returns `OK`.
4. **Write Intentional Commit Messages**: Answer the question: *"If applied, this commit will..."* in 50 characters or less for the title.
5. **Protect Your Main Branch**: Enforce branch protection rules on GitHub requiring peer reviews, passing status checks, and up-to-date branches before merging.

