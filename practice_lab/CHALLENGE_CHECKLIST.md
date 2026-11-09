# 🏆 Git & GitHub Mastery: 36-Challenge Verification Checklist

> **Student Portfolio Verification & Evaluation Matrix**  
> **Curriculum**: Week 3 — Version Control, Collaboration and Professional Development Workflow  
> **Specialization**: B.Tech Robotics & Artificial Intelligence

Track your practical mastery across all 12 modules by completing each challenge in your local workspace. Check off each box as you verify the corresponding skill.

---

## 📌 Section 1: Setup, Configuration & Architecture (Labs 01 & 02)
- [ ] **Challenge 01**: Configure global Git identity (`user.name` and `user.email`) and set default branch to `main`.
- [ ] **Challenge 02**: Initialize a local repository (`git init`) and inspect `.git/HEAD`, `.git/config`, and `.git/objects/`.
- [ ] **Challenge 03**: Verify `.gitignore` rules using `git check-ignore -v` against `.pyc` and `__pycache__` files.
- [ ] **Challenge 04**: Distinguish between unstaged changes (`git diff`) and staged changes (`git diff --staged`).
- [ ] **Challenge 05**: Stage changes interactively using patch mode (`git add -p`).
- [ ] **Challenge 06**: Craft an atomic Conventional Commit (`feat:`, `fix:`, `docs:`, `chore:`).
- [ ] **Challenge 07**: Amend the most recent commit message and staged files using `git commit --amend`.

---

## 📌 Section 2: Branching & Context Switching (Lab 03 & Branching Guide)
- [ ] **Challenge 08**: Create and switch to a new branch using modern syntax (`git switch -c <name>`).
- [ ] **Challenge 09**: Verify that switching branches updates the working tree files to match the target commit snapshot.
- [ ] **Challenge 10**: Configure a custom Git alias (`git config --global alias.tree "log --graph --oneline --decorate --all"`).
- [ ] **Challenge 11**: Identify merged vs unmerged branches using `git branch --merged` and `git branch --no-merged`.
- [ ] **Challenge 12**: Delete a merged feature branch safely using `git branch -d`.

---

## 📌 Section 3: Merging & Conflict Resolution (Lab 04 & Merge Conflict Guide)
- [ ] **Challenge 13**: Perform a clean Fast-Forward (FF) merge.
- [ ] **Challenge 14**: Intentionally orchestrate a merge conflict on `src/greeting.py`.
- [ ] **Challenge 15**: Identify and explain the conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`).
- [ ] **Challenge 16**: Abort an active merge conflict cleanly using `git merge --abort`.
- [ ] **Challenge 17**: Resolve a merge conflict manually, run unit tests to verify behavior, and commit the resolution.

---

## 📌 Section 4: Undo Operations & Disaster Recovery (Lab 05)
- [ ] **Challenge 18**: Discard unstaged changes in a modified file using `git restore <file>`.
- [ ] **Challenge 19**: Unstage a staged file without losing working directory modifications using `git restore --staged <file>`.
- [ ] **Challenge 20**: Safely undo a public commit using `git revert HEAD --no-edit`.
- [ ] **Challenge 21**: Temporarily shelve in-progress work with `git stash` and restore it using `git stash pop`.
- [ ] **Challenge 22**: Simulate an accidental `git reset --hard HEAD~1` and resurrect the commit using `git reflog`.

---

## 📌 Section 5: Remote Operations & Pull Requests (Labs 06 & 07)
- [ ] **Challenge 23**: Add a remote GitHub repository (`git remote add origin <url>`) and configure upstream tracking (`-u`).
- [ ] **Challenge 24**: Differentiate between `git fetch` and `git pull`, inspecting incoming remote commits before merging.
- [ ] **Challenge 25**: Push a feature branch and open a Pull Request using `.github/PULL_REQUEST_TEMPLATE.md`.
- [ ] **Challenge 26**: Address a review suggestion, commit the change to the branch, and verify GitHub updates the PR.
- [ ] **Challenge 27**: Squash and merge the Pull Request on GitHub and delete the remote branch.

---

## 📌 Section 6: Advanced Collaboration & Forensics (Labs 08, 09 & 10)
- [ ] **Challenge 28**: Simulate two engineers (Alice & Bob) locally using a bare repository and resolve a push rejection with `git pull --rebase`.
- [ ] **Challenge 29**: Inspect author attribution using `git blame -L` and commit history using pickaxe (`git log -S`).
- [ ] **Challenge 30**: Execute automated binary search debugging using `git bisect run python -m unittest discover tests`.
- [ ] **Challenge 31**: Create an annotated release tag (`git tag -a v1.0.0 -m "..."`) and inspect tagger metadata with `git show`.
- [ ] **Challenge 32**: Push tags to GitHub (`git push origin --tags`) and publish an official GitHub Release.

---

## 📌 Section 7: Rebasing & Automation Gates (Labs 11 & 12)
- [ ] **Challenge 33**: Perform an interactive rebase (`git rebase -i HEAD~3`) to squash and reword interim commits into a clean unit.
- [ ] **Challenge 34**: Surgically backport an isolated commit across branches using `git cherry-pick <hash>`.
- [ ] **Challenge 35**: Author an automated `.git/hooks/pre-commit` script that triggers unit tests prior to recording commits.
- [ ] **Challenge 36**: Verify that the pre-commit hook automatically blocks broken commits and permits clean commits.

---

## 🎓 Completion Certificate Sign-Off
- **Student Name**: ___________________________
- **Date Completed**: ___________________________
- **Repository URL**: ___________________________
- **Verified By**: ___________________________
