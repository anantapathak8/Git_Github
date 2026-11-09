# ⏪ Lab 05: Undo Mechanisms, Stashing & Disaster Recovery

> **Objective**: Master safe and destructive undo operations; distinguish between `git restore`, `git reset`, and `git revert`; use `git stash` for agile task switching; and recover supposedly "lost" commits using `git reflog`.

---

## 📋 Prerequisites
1. Completion of Lab 04.
2. Clean working tree on `main` (`git status` shows clean).
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: The Undo Hierarchy

Git offers multiple tools to rewind time depending on where your changes currently reside:

| Scope | Scenario | Recommended Command | Safety Level |
| :--- | :--- | :--- | :--- |
| **Working Directory** | Discard uncommitted edits in a file | `git restore <file>` | ⚠️ Destructive (Unrecoverable) |
| **Staging Area** | Unstage a file without losing edits | `git restore --staged <file>` | 🟢 Completely Safe |
| **Local Commits** | Undo recent commit(s) before pushing | `git reset --soft / --mixed` | 🟢 Safe (Preserves code) |
| **Shared Commits** | Undo a commit already on remote/main | `git revert <commit-hash>` | 🟢 Safe (Creates inverse commit) |
| **Interrupted Work** | Temporarily shelve unfinished edits | `git stash` | 🟢 Safe & Reversible |
| **Disaster Recovery**| Resurrect deleted branches/commits | `git reflog` + `git reset` | 🛡️ The Ultimate Lifesaver |

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 5.1: Discarding Changes with `git restore`

Make an accidental edit in `src/calculator.py` (e.g. append `# temporary scratch line`):

Check status in PowerShell:
```powershell
git status
```

Discard unstaged changes in that file:
```powershell
git restore src/calculator.py
```
Check `git status` again—the file is restored to its pristine condition!

Now stage an edit:
```powershell
# Append a comment to calculator.py
Add-Content -Path src/calculator.py -Value "# Staged test comment"
git add src/calculator.py
```

Unstage the file back to the working tree:
```powershell
git restore --staged src/calculator.py
```
The file is moved from Staged back to Modified in your Working Tree.

Discard the scratch edit:
```powershell
git restore src/calculator.py
```

---

### Task 5.2: The Three Flavors of `git reset`

Suppose you made a commit that you want to undo locally:

```
HEAD~1 ──────> [Previous Commit]
HEAD   ──────> [Commit to Undo]
```

1. **`git reset --soft HEAD~1`**:
   - Moves branch pointer back one commit.
   - **Leaves all changed files staged in your Index**.
   - Ideal when you want to re-commit with a better message or combine with new files.

2. **`git reset --mixed HEAD~1` (Default)**:
   - Moves branch pointer back one commit.
   - **Unstages changes but keeps them in your Working Directory**.
   - Ideal when you want to restructure your commits.

3. **`git reset --hard HEAD~1`**:
   - Moves pointer back.
   - **Wipes out both the staging index AND your working tree edits!**
   - ⚠️ Use with extreme caution.

---

### Task 5.3: Safe Public Undo with `git revert`
If a bad commit was already pushed to a public remote, **never use reset**. Instead, use `git revert`:

```powershell
# Create a dummy test commit
Add-Content -Path src/calculator.py -Value "# Temporary test probe"
git add src/calculator.py
git commit -m "chore: add temporary test probe"

# Revert it safely
git revert HEAD --no-edit
```

Inspect `git log -n 2 --oneline`:
```text
3e4f5a6 (HEAD -> main) Revert "chore: add temporary test probe"
1b2c3d4 chore: add temporary test probe
```
Git recorded a brand new commit that performs the exact inverse of the reverted commit! Public history remains unbroken.

---

### Task 5.4: Stashing In-Progress Work
Imagine you are halfway through writing a new function and an urgent request arises.

Make an uncommitted edit to `src/calculator.py`:
```powershell
Add-Content -Path src/calculator.py -Value "def experimental_kalman_filter():"
```

Shelve your unfinished work:
```powershell
git stash save "WIP: experimental kalman filter formulation"
```

Check status:
```powershell
git status
```
Working tree is completely clean! You can now switch branches or pull updates safely.

Inspect your stashed items:
```powershell
git stash list
```

**Expected Output:**
```text
stash@{0}: On main: WIP: experimental kalman filter formulation
```

When ready to resume work:
```powershell
git stash pop
```
Your experimental code is restored immediately! Discard it:
```powershell
git restore src/calculator.py
```

---

### Task 5.5: Time Travel with `git reflog` (Disaster Recovery)

What if you accidentally ran `git reset --hard` and panicked, believing all work was erased?

Test this in a safe simulation:

```powershell
# 1. Create a valuable commit
Add-Content -Path src/calculator.py -Value "# Robotic Sensor V3 Driver"
git add src/calculator.py
git commit -m "feat(sensor): valuable sensor driver code"

# 2. Note the commit hash (e.g., 'a1b2c3d')
git log -n 1 --oneline

# 3. Simulate accidental hard reset!
git reset --hard HEAD~1

# 4. Check git log: the commit is GONE from standard history!
git log -n 2 --oneline
```

Now summon the **Reference Log (reflog)**:
```powershell
git reflog
```

**Expected Output:**
```text
b2c3d4e HEAD@{0}: reset: moving to HEAD~1
a1b2c3d HEAD@{1}: commit: feat(sensor): valuable sensor driver code
...
```

Git never deletes commits immediately! The reflog tracks every movement of `HEAD`.

**Rescue the commit:**
```powershell
# Point HEAD back to the lost commit SHA!
git reset --hard HEAD@{1}
```

Check `git log`:
```powershell
git log -n 1 --oneline
```
The "lost" commit is fully resurrected!

Clean up our test probe:
```powershell
git reset --hard HEAD~1
```

---

## 🔍 Verification Steps
1. Run `git status` — confirm working tree is clean.
2. Run `python -m unittest discover tests` — all unit tests pass with `OK`.
3. Run `git reflog -n 5` — observe the log entries tracking your reset and recovery.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `git reset --hard` wiped uncommitted work | Working tree files were never committed or stashed. | Git only tracks committed snapshots in reflog. Uncommitted deleted edits cannot be recovered via Git. |
| Stash conflict on pop | The active branch modified the same lines stored in the stash. | Resolve conflict markers, stage file with `git add`, and run `git stash drop` to clear the stash entry. |
| Using `git reset` on public branches | Rewrites commit history that teammates have already pulled. | Use `git revert <commit-hash>` instead. |

---

## ✅ Completion Checklist
- [ ] Discarded working tree edits using `git restore <file>`.
- [ ] Unstaged files without data loss using `git restore --staged <file>`.
- [ ] Compared `--soft`, `--mixed`, and `--hard` reset modes.
- [ ] Created and verified a public undo using `git revert`.
- [ ] Shelved and restored in-progress work using `git stash` and `git stash pop`.
- [ ] Resurrected a supposedly lost commit using `git reflog`.
