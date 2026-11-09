# 🛠 Lab 01: Repository Setup, Configuration & Internals

> **Objective**: Initialize a Git repository, configure developer identity, verify `.gitignore` behavior, explore the hidden `.git` internal architecture, and create the repository's foundational commit.

---

## 📋 Prerequisites
Before starting this lab:
1. Windows PowerShell 5.1+ or PowerShell 7 installed.
2. Git 2.23+ installed (`git --version`).
3. Python 3.8+ installed (`python --version`).
4. Workspace opened at `C:\Users\anant\OneDrive\Desktop\Git_GitHub_Week03`.
5. Codebase integrity verified (`python -m unittest discover tests` returns `OK`).

---

## 📖 Theoretical Context: What Happens During `git init`?

When you initialize a repository, Git creates a hidden directory named `.git/`. This directory is the **Object Database and Administrative Engine** of your project. The files outside `.git/` are merely your working tree.

Key components inside `.git/`:
- `HEAD`: A file with a reference pointer indicating your current checked-out branch or commit.
- `config`: Repository-specific configuration settings overriding global flags.
- `objects/`: Content-addressable store containing compressed zlib blobs (file contents), trees (directory manifests), and commits.
- `refs/`: Pointers to commit objects (branches in `refs/heads/`, tags in `refs/tags/`).
- `index`: The staging area binary cache (created on first `git add`).

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 1.1: Configure Global and Local Identity
Git stamps every commit with an author name and email. Set these up:

```powershell
# Set global identity (applies across all repositories on this computer)
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"

# Set default initial branch name to modern standard 'main'
git config --global init.defaultBranch main

# Set consistent cross-platform line ending behavior for Windows
git config --global core.autocrlf true
```

Verify your active settings and their origins:
```powershell
git config --list --show-origin
```

**Expected Output:**
```text
file:C:/Users/anant/.gitconfig  user.name=Your Name
file:C:/Users/anant/.gitconfig  user.email=your.email@university.edu
file:C:/Users/anant/.gitconfig  init.defaultbranch=main
file:C:/Users/anant/.gitconfig  core.autocrlf=true
```

---

### Task 1.2: Initialize the Repository
Ensure you are in the project root (`Git_GitHub_Week03`):

```powershell
git init
```

**Expected Output:**
```text
Initialized empty Git repository in C:/Users/anant/OneDrive/Desktop/Git_GitHub_Week03/.git/
```

Check repository status:
```powershell
git status
```

**Expected Output:**
```text
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.github/
	.gitignore
	BRANCHING_EXERCISE.md
	CHANGELOG.md
	CONTRIBUTING.md
	GIT_CHEATSHEET.md
	GIT_WORKFLOW.md
	LICENSE
	MERGE_CONFLICT_GUIDE.md
	PULL_REQUEST_GUIDE.md
	README.md
	practice_lab/
	requirements-dev.txt
	src/
	tests/

nothing added to commit but untracked files present (use "git add" to track)
```

---

### Task 1.3: Inspect the `.git` Anatomy
Explore the newly generated `.git` directory in PowerShell:

```powershell
Get-ChildItem -Path .git -Force
```

Read what `HEAD` points to:
```powershell
Get-Content .git/HEAD
```

**Expected Output:**
```text
ref: refs/heads/main
```
This confirms `HEAD` is pointing to the `main` branch pointer.

---

### Task 1.4: Test `.gitignore` Rules
Verify that unwanted files and compiled caches are properly ignored:

Create a temporary dummy cache file:
```powershell
New-Item -Path "src/calculator.pyc" -ItemType File
```

Now run `git status`:
```powershell
git status
```
Notice that `src/calculator.pyc` is **not** listed under untracked files!

Verify which ignore rule matched:
```powershell
git check-ignore -v src/calculator.pyc
```

**Expected Output:**
```text
.gitignore:3:*.py[cod]	src/calculator.pyc
```

Remove the temporary file:
```powershell
Remove-Item "src/calculator.pyc"
```

---

### Task 1.5: Stage and Create the Initial Commit
Stage all tracked project files:
```powershell
git add .
```

Verify the staging area:
```powershell
git status
```
You will see `new file: ...` in green for all project files.

Commit with a Conventional Commit message:
```powershell
git commit -m "chore: initial repository setup with core modules, tests, and documentation"
```

**Expected Output:**
```text
[main (root-commit) 9d4e12a] chore: initial repository setup with core modules, tests, and documentation
 24 files changed, 2100 insertions(+)
 create mode 100644 .github/workflows/ci.yml
 ...
```

Inspect your commit log:
```powershell
git log --oneline
```

**Expected Output:**
```text
9d4e12a (HEAD -> main) chore: initial repository setup with core modules, tests, and documentation
```

---

## 🔍 Verification Steps
1. Run `git status` — must output `nothing to commit, working tree clean`.
2. Run `git log -1 --stat` — verify that all project files are included in the initial commit.
3. Run `git branch --show-current` — must output `main`.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `fatal: not a git repository` | Command executed outside the repo root or `.git` was deleted. | Navigate to the correct directory (`cd C:\Users\anant\OneDrive\Desktop\Git_GitHub_Week03`) or run `git init`. |
| Author shows generic `User@PC` | Identity was not configured before making the commit. | Run `git config --global user.name` and `user.email`, then run `git commit --amend --reset-author --no-edit`. |
| Default branch is `master` instead of `main` | Global init branch was not configured prior to `git init`. | Rename the branch: `git branch -M main`. |
| Untracked `.pyc` or `.venv` files appear in `git status` | Files were created before `.gitignore` or rule syntax is incorrect. | Verify `.gitignore` exists in root and matches file path pattern. |

---

## ✅ Completion Checklist
- [ ] Configured global author name and email in Git.
- [ ] Initialized repository and verified `.git` folder structure.
- [ ] Verified `.gitignore` rule execution with `git check-ignore`.
- [ ] Staged all workspace files with `git add .`.
- [ ] Created initial commit with semantic commit message.
- [ ] Verified clean working tree with `git status` and inspected `git log`.
