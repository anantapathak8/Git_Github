# 🧪 Git & GitHub Hands-on Practice Lab

> **Week 3 Portfolio Project — Practical Mastery Lab**  
> **Specialization**: B.Tech Robotics & Artificial Intelligence  
> **Course**: Version Control, Collaboration, and Professional Engineering Workflows

---

## 🎯 Lab Overview & Roadmap

This hands-on laboratory is organized into **12 sequential, progressive challenge modules**. Each module bridges software engineering theory with real terminal practice using the Python demonstration modules (`src/calculator.py` and `src/greeting.py`) in this workspace.

```
+---------------------------------------------------------------------------------------------------+
|                                  THE 12-STAGE GIT MASTERY ROADMAP                                 |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [01: Repo Setup]       --> [02: Commit Mastery]   --> [03: Branching]    --> [04: Merging]        |
|   - Identity & Config        - Staging & Index          - Parallel Streams     - 3-Way & FF       |
|   - Anatomy of .git          - Conventional Commits     - Context Switching    - Conflict Fix     |
|                                                                                                   |
|                                                                                                   |
|  [05: Undo & Recovery]  --> [06: Remote Ops]       --> [07: Pull Requests]--> [08: Collab Sim]    |
|   - Reset, Revert, Stash     - GitHub Remote Link       - PR Templates         - Alice & Bob      |
|   - Reflog time machine      - Push, Fetch, Pull        - Code Reviews         - Multi-Dev        |
|                                                                                                   |
|                                                                                                   |
|  [09: History Forensics]--> [10: Tags & Releases]  --> [11: Rebasing]     --> [12: Git Hooks]     |
|   - Git blame & log          - SemVer v1.0.0            - Interactive Rebase   - Pre-Commit Gates |
|   - Bisect regression hunt   - Annotated Releases       - Cherry-Pick          - Auto-Test Guard  |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

---

## 📚 Lab Module Directory (All 12 Practical Challenges)

| Module | Title | Primary Commands Practiced |
| :---: | :--- | :--- |
| **[01](01_repository_setup.md)** | **Repository Initialization & Config** | `git init`, `git config`, `git status`, `.gitignore` |
| **[02](02_commit_mastery.md)** | **Commit Mastery & Staging Mechanics** | `git add -p`, `git diff`, `git diff --staged`, `git commit --amend` |
| **[03](03_branching.md)** | **Branching Lifecycle & Parallel Tracks** | `git switch -c`, `git branch -v`, `git branch -d` |
| **[04](04_merging_and_conflicts.md)** | **Merging & Conflict Resolution** | `git merge`, `git merge --abort`, conflict marker cleanup |
| **[05](05_undo_and_recovery.md)** | **Undo, Stashing & Disaster Recovery** | `git restore`, `git reset`, `git revert`, `git stash`, `git reflog` |
| **[06](06_remote_operations.md)** | **Remote Operations & Synchronization** | `git remote add`, `git push -u`, `git fetch`, `git pull` |
| **[07](07_pull_requests.md)** | **Pull Request Lifecycle & Reviews** | `gh pr create`, PR templates, branch reviews |
| **[08](08_collaboration_simulation.md)** | **Multi-Developer Simulation** | Local multi-identity simulation (Alice & Bob), `git pull --rebase` |
| **[09](09_history_investigation.md)** | **Code Forensics & Bisect Debugging** | `git log -S`, `git blame -L`, `git bisect run` |
| **[10](10_tags_and_releases.md)** | **Semantic Versioning & Releases** | `git tag -a`, `git push --tags`, GitHub Releases |
| **[11](11_rebasing_and_cherry_pick.md)** | **Linear History & Cherry-Picking** | `git rebase -i`, squash, reword, `git cherry-pick` |
| **[12](12_git_hooks_and_automation.md)** | **Client-Side Quality Gates & Hooks** | `.git/hooks/pre-commit`, automated test runner |
| **[Checklist](CHALLENGE_CHECKLIST.md)** | **Master Challenge Verification** | 30 Hands-On Practical Challenges |

---

## 📖 Deep-Dive Reference Guides
- **[BRANCHING_EXERCISE.md](../BRANCHING_EXERCISE.md)**: Extended parallel branch simulation.
- **[MERGE_CONFLICT_GUIDE.md](../MERGE_CONFLICT_GUIDE.md)**: Deep dive on conflict markers and resolution heuristics.
- **[GIT_CHEATSHEET.md](../GIT_CHEATSHEET.md)**: Fast terminal reference card.

---

## ⚙️ Prerequisites & Environment Verification

Before starting Lab 01, run these checks in your terminal:

```powershell
# 1. Verify Git Installation
git --version
# Recommended: git version 2.23.0 or higher

# 2. Verify Python Installation
python --version
# Expected: Python 3.8+

# 3. Verify Codebase Integrity
python -m unittest discover tests
# Expected: OK (All 31 tests pass)
```

Proceed to **[Lab 01: Repository Setup](01_repository_setup.md)** to begin!
