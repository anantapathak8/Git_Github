# 🌐 Lab 06: Remote Operations & GitHub Synchronization

> **Objective**: Connect a local repository to GitHub, configure upstream tracking, differentiate between `git fetch` and `git pull`, understand remote tracking branches (`origin/main`), and configure authentication.

---

## 📋 Prerequisites
1. Completion of Lab 05.
2. A GitHub account created at [github.com](https://github.com).
3. Local repository on `main` branch with clean working tree.

---

## 📖 Theoretical Context: Distributed Architecture

Git is distributed. Your local repository inside `.git` is completely autonomous. The remote repository on GitHub is simply another clone designated as the canonical hub (`origin`).

```
+------------------------------------+               +------------------------------------+
|          Local Machine             |               |               GitHub               |
|                                    |   git push    |                                    |
| [Local main]  ---> [origin/main]   | ------------> | [Remote main]                      |
|                     ^ (Tracking)   |   git fetch   |                                    |
|                     +--------------+ <------------ |                                    |
+------------------------------------+               +------------------------------------+
```

### Remote Tracking Branches:
`origin/main` is a read-only local bookmark pointing to the last known state of `main` on GitHub.
- `git fetch`: Updates your local bookmark `origin/main` with changes from GitHub. It **never touches** your working tree files.
- `git pull`: Executes `git fetch` followed immediately by `git merge origin/main`.

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 6.1: GitHub Authentication (SSH vs PAT)

To push code to GitHub securely:

#### Option A: SSH Key (Recommended for Engineers)
Generate and register an Ed25519 SSH Key in PowerShell:
```powershell
# 1. Generate an Ed25519 SSH Key
ssh-keygen -t ed25519 -C "your.email@university.edu"

# 2. Start SSH Agent and add your key in PowerShell
Start-Service ssh-agent
ssh-add $HOME/.ssh/id_ed25519

# 3. Copy public key to clipboard:
Get-Content $HOME/.ssh/id_ed25519.pub | Set-Clipboard
# Paste into GitHub -> Settings -> SSH and GPG Keys -> New SSH Key
```

#### Option B: Personal Access Token (PAT)
If using HTTPS, GitHub requires a Personal Access Token (PAT) with `repo` scope instead of your account password.

---

### Task 6.2: Linking to a Remote Repository

Create a new empty repository on GitHub named `Git_GitHub_Week03` (leave "Initialize with README" unchecked).

Link your local repository to GitHub:
```powershell
# Replace <YOUR-GITHUB-USERNAME> with your actual GitHub username
git remote add origin https://github.com/<YOUR-GITHUB-USERNAME>/Git_GitHub_Week03.git

# Or with SSH:
# git remote add origin git@github.com:<YOUR-GITHUB-USERNAME>/Git_GitHub_Week03.git
```

Verify configured remotes:
```powershell
git remote -v
```

**Expected Output:**
```text
origin  https://github.com/<username>/Git_GitHub_Week03.git (fetch)
origin  https://github.com/<username>/Git_GitHub_Week03.git (push)
```

---

### Task 6.3: Pushing with Upstream Tracking (`-u`)
The first time you push a branch, establish upstream tracking using `-u` (or `--set-upstream`):

```powershell
git push -u origin main
```

Why is `-u` essential?
It binds your local `main` branch to `origin/main`. Future pushes and pulls require only:
```powershell
git push
git pull
```

---

### Task 6.4: Fetch vs Pull in Action

Suppose a teammate pushed a commit to GitHub. To inspect their changes before integrating:

```powershell
# Fetch remote commits without merging into working tree
git fetch origin

# Inspect commits that exist on remote but not locally
git log main..origin/main --oneline

# View diff between your code and remote code
git diff main origin/main
```

When satisfied, merge remote changes:
```powershell
git merge origin/main
```

Or execute fetch + rebase in a single clean pass:
```powershell
git pull --rebase origin main
```

---

### Task 6.5: Diagnosing Rejected Pushes (Non-Fast-Forward)
If you attempt to push when GitHub has new commits:
```text
To https://github.com/...
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '...'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

**How to resolve cleanly**:
```powershell
# Fetch and rebase your work on top of remote changes
git pull --rebase origin main

# Once rebase succeeds, push cleanly
git push origin main
```

> ⚠️ **Avoid `git push --force`!** Overwriting remote history can delete teammates' work. Always use `git pull --rebase` or `--force-with-lease`.

---

## 🔍 Verification Steps
1. Run `git remote show origin` — verify tracking branch status and fetch/push URLs.
2. Open your GitHub repository URL in your web browser — confirm all files, commits, and directories are visible.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `Support for password authentication was removed` | Using GitHub account password instead of PAT over HTTPS. | Generate a Personal Access Token in GitHub Settings -> Developer settings -> Tokens (Classic) with `repo` scope, or switch to SSH. |
| `fatal: remote origin already exists` | Attempting to run `git remote add origin` twice. | Check existing with `git remote -v`. Update with `git remote set-url origin <new-url>`. |
| Push rejected (non-fast-forward) | Remote branch has commits not present locally. | Run `git pull --rebase origin main`, resolve any conflicts, then run `git push`. |

---

## ✅ Completion Checklist
- [ ] Configured GitHub authentication via SSH key or Personal Access Token.
- [ ] Linked local repository to remote GitHub URL with `git remote add origin`.
- [ ] Pushed main branch with upstream tracking (`git push -u origin main`).
- [ ] Understood difference between `git fetch` (inspection) and `git pull` (fetch + merge).
- [ ] Verified remote synchronization on GitHub.
