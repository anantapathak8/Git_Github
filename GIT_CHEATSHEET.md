# ⚡ The Definitive Professional Git Cheat Sheet

> **Robotics & AI Engineering Curriculum — Week 3 Reference**  
> Complete reference card for daily terminal workflows, branching, merge conflict resolution, and forensics in Windows PowerShell.

---

## 📑 Quick Navigation
1. [Configuration & Developer Identity](#1-configuration--developer-identity)
2. [Repository Setup & Initialization](#2-repository-setup--initialization)
3. [The Staging Area & Everyday Snapshotting](#3-the-staging-area--everyday-snapshotting)
4. [Branching & Context Switching](#4-branching--context-switching)
5. [Merging & Integration](#5-merging--integration)
6. [Rebasing & History Crafting](#6-rebasing--history-crafting)
7. [Undoing Mistakes & Disaster Recovery](#7-undoing-mistakes--disaster-recovery)
8. [Code Forensics, Blame & Bisect Debugging](#8-code-forensics-blame--bisect-debugging)
9. [Remote Repositories & GitHub Synchronization](#9-remote-repositories--github-synchronization)
10. [Semantic Versioning & Releases](#10-semantic-versioning--releases)
11. [Essential PowerShell Aliases & Pro Tips](#11-essential-powershell-aliases--pro-tips)

---

## 1. Configuration & Developer Identity

```powershell
# Set global identity (stored in ~/.gitconfig)
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"

# Set repository-local identity (stored in .git/config, overrides global)
git config --local user.name "Robotics Team Operator"
git config --local user.email "operator@robotics.lab"

# Set standard default initial branch
git config --global init.defaultBranch main

# Windows line-ending handling (CRLF on checkout, LF on commit)
git config --global core.autocrlf true

# Display all active configs and their file sources
git config --list --show-origin
```

---

## 2. Repository Setup & Initialization

```powershell
# Initialize a brand-new Git repository in current folder
git init

# Initialize with explicit branch name
git init -b main

# Clone an existing remote repository
git clone https://github.com/username/repository.git

# Clone into a custom directory name
git clone https://github.com/username/repository.git my_custom_dir

# Check if a file is being ignored by .gitignore and find out why
git check-ignore -v src/temp_file.pyc
```

---

## 3. The Staging Area & Everyday Snapshotting

```powershell
# Inspect working tree and staging index status
git status

# Compact, two-character status view
git status -s

# View differences between working tree and staging area
git diff

# View differences between staging area and HEAD commit
git diff --staged
# (Synonym: git diff --cached)

# View diff of a specific file
git diff src/calculator.py

# Stage a specific file
git add src/calculator.py

# Stage all modified and new files (excluding ignored files)
git add .

# Interactively review and stage code hunks (patch mode)
git add -p

# Commit staged changes with Conventional Commit message
git commit -m "feat(calc): implement 2D euclidean distance function"

# Stage all tracked modified files and commit in one step
git commit -am "fix(greeting): resolve whitespace bug in user banner"

# Amend the last commit (modify message or include newly staged files)
git commit --amend -m "feat(calc): implement euclidean distance with validation"
```

---

## 4. Branching & Context Switching

```powershell
# List local branches (* indicates current branch)
git branch

# List local branches with latest commit SHA and subject line
git branch -v

# List all branches including remote tracking branches
git branch -a

# Create and switch to a new branch (Git 2.23+ modern syntax)
git switch -c feature/robot-telemetry

# Switch to an existing branch
git switch main

# Legacy checkout command (equivalent to git switch -c)
git checkout -b feature/robot-telemetry

# List branches already merged into current branch
git branch --merged

# List branches containing unmerged work
git branch --no-merged

# Safely delete a merged branch (blocks if unmerged)
git branch -d feature/robot-telemetry

# Force-delete an unmerged branch (destructive!)
git branch -D feature/abandoned-experiment
```

---

## 5. Merging & Integration

```powershell
# Fast-Forward or 3-Way merge branch into active branch
git merge feature/robot-telemetry

# Merge with an explicit non-fast-forward merge commit
git merge --no-ff feature/robot-telemetry -m "merge: integrate robot telemetry feature"

# Abort an active merge conflict and restore pristine pre-merge state
git merge --abort

# Conclude a merge after manually resolving conflict markers and staging
git commit
```

---

## 6. Rebasing & History Crafting

```powershell
# Rebase current branch on top of main (creates linear history)
git rebase main

# Interactive rebase of the last 4 commits (squash, edit, reword, drop)
git rebase -i HEAD~4

# Continue rebase after resolving conflict markers and running `git add`
git rebase --continue

# Abort a rebase and restore prior branch state
git rebase --abort

# Cherry-pick a specific commit from another branch into current branch
git cherry-pick 7a8b9c0
```

---

## 7. Undoing Mistakes & Disaster Recovery

```powershell
# Discard uncommitted modifications in a specific file
git restore src/calculator.py

# Unstage a file back to working tree without losing modifications
git restore --staged src/calculator.py

# Undo commit, KEEP changes staged in index
git reset --soft HEAD~1

# Undo commit, UNSTAGE changes to working tree (default)
git reset --mixed HEAD~1

# Undo commit and PERMANENTLY ERASE changes (use with caution!)
git reset --hard HEAD~1

# Create a new commit that inverts the changes of a previous commit (safe for public branches!)
git revert <commit-hash> --no-edit

# Temporarily shelve uncommitted work
git stash save "WIP: sensor calibration refactor"

# List all stashed modification sets
git stash list

# Re-apply most recent stash and remove it from stack
git stash pop

# Re-apply most recent stash while KEEPING it in the stack
git stash apply

# Clear all stashes
git stash clear

# THE ULTIMATE LIFESAVER: View all local HEAD movements
git reflog

# Resurrect a lost commit found in reflog
git reset --hard HEAD@{2}
```

---

## 8. Code Forensics, Blame & Bisect Debugging

```powershell
# View commit history as a one-line summary
git log --oneline

# Graphical ASCII representation of branch topology
git log --graph --oneline --decorate --all

# View the last 5 commits with patch diffs
git log -p -n 5

# Search commit messages for a keyword
git log --grep="telemetry" --oneline

# Search commit history for when a specific string was added/removed (Pickaxe)
git log -S "calculate_mean" --oneline

# Filter commits by author
git log --author="Alice" --oneline

# Filter commits within date boundary
git log --since="2.weeks.ago" --until="yesterday"

# Inspect who authored which line of code and when
git blame src/calculator.py

# Inspect blame for a specific line range
git blame -L 20,40 src/calculator.py

# Start automated binary search regression hunt
git bisect start
git bisect bad                  # Mark current commit as broken
git bisect good <commit-hash>   # Mark historical known-good commit

# Automatically run test suite at each bisect step!
git bisect run python -m unittest discover tests

# Conclude bisect session and return to original branch
git bisect reset
```

---

## 9. Remote Repositories & GitHub Synchronization

```powershell
# Add a remote named 'origin'
git remote add origin https://github.com/username/Git_GitHub_Week03.git

# Display remote URLs
git remote -v

# Push branch and configure upstream tracking (-u)
git push -u origin main

# Standard push (once upstream tracking is established)
git push

# Fetch latest commits from remote without merging
git fetch origin

# Inspect incoming remote commits before merging
git log main..origin/main --oneline

# Merge remote changes into local branch
git merge origin/main

# Fetch and rebase local commits on top of remote in one step
git pull --rebase origin main

# Safe force-push that protects against overwriting teammates' commits
git push --force-with-lease origin feature/my-branch

# Delete a remote branch on GitHub
git push origin --delete feature/my-branch

# Clean up stale remote-tracking branch references
git remote prune origin
```

---

## 10. Semantic Versioning & Releases

```powershell
# List all tags
git tag

# Create an annotated release tag (RECOMMENDED for production releases)
git tag -a v1.0.0 -m "Release v1.0.0: Initial stable release with full test suite"

# Inspect tag metadata, tagger identity, and commit details
git show v1.0.0

# Tag a past historical commit
git tag -a v0.9.0 9d4e12a -m "Beta release"

# Push a specific tag to GitHub
git push origin v1.0.0

# Push all local tags to GitHub simultaneously
git push origin --tags

# Delete a tag locally
git tag -d v0.9.0

# Delete a tag on remote GitHub
git push origin --delete v0.9.0
```

---

## 11. Essential PowerShell Aliases & Pro Tips

Add these aliases to your PowerShell profile or Git configuration to accelerate your daily workflow:

```powershell
# Add Git Aliases (run once in terminal)
git config --global alias.st "status -s"
git config --global alias.tree "log --graph --oneline --decorate --all"
git config --global alias.co "switch"
git config --global alias.cob "switch -c"
git config --global alias.br "branch -v"
git config --global alias.ci "commit -m"
git config --global alias.amend "commit --amend --no-edit"
git config --global alias.last "log -1 HEAD --stat"

# Now you can run:
# git st
# git tree
# git cob feature/new-idea
# git amend
```

> 💡 **Golden Rule of Git**: Treat your local Git history as a private scratchpad (commit small, amend freely, rebase locally), but treat pushed public branches as immutable shared history (never rebase or force-push over public main!).

