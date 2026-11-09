# 🤖 Lab 12: Client-Side Quality Gates & Git Hooks

> **Objective**: Understand Git hooks architecture; create an automated `pre-commit` hook in Windows PowerShell that executes the Python unit test suite before allowing commits; and prevent regressions before they reach your repository.

---

## 📋 Prerequisites
1. Completion of Lab 11.
2. Clean working tree on `main` in `Git_GitHub_Week03`.
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Git Hooks as Quality Gates

A Git Hook is a script that Git executes automatically when specific lifecycle events occur (e.g. `pre-commit`, `commit-msg`, `pre-push`).

Hooks reside inside `.git/hooks/`:
- **`pre-commit`**: Runs *before* a commit is recorded. If the script exits with a non-zero code (`exit 1`), Git immediately **aborts the commit**!
- **`commit-msg`**: Validates that commit messages adhere to Conventional Commits standards.
- **`pre-push`**: Runs before code is uploaded to GitHub.

In robotics and AI engineering, pre-commit hooks ensure that failing motor tests or syntax errors can never be committed by accident.

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 12.1: Inspect Sample Hooks
Inspect the sample scripts provided inside `.git/hooks/` using PowerShell:

```powershell
Get-ChildItem -Path .git/hooks/
```
*(Notice the `.sample` extensions; removing the `.sample` extension activates the hook).*

---

### Task 12.2: Create an Automated `pre-commit` Hook
Create an executable `pre-commit` hook that runs Python unit tests:

In PowerShell:
```powershell
# Write the pre-commit script into .git/hooks/pre-commit
$hookScript = @'
#!/bin/sh
echo "🔍 [GIT HOOK] Executing automated pre-commit unit test verification..."
python -m unittest discover tests
RESULT=$?

if [ $RESULT -ne 0 ]; then
    echo "❌ [GIT HOOK] Tests failed! Commit aborted to preserve repository integrity."
    exit 1
fi

echo "✅ [GIT HOOK] All unit tests passed. Proceeding with commit."
exit 0
'@

Set-Content -Path ".git/hooks/pre-commit" -Value $hookScript -NoNewline
```

---

### Task 12.3: Test the Hook with Passing Code
Make a valid modification in `src/calculator.py`:

```powershell
Add-Content -Path src/calculator.py -Value "# Verified pre-commit compatibility"
git add src/calculator.py
git commit -m "chore: test pre-commit hook with clean tests"
```

**Expected Output:**
```text
🔍 [GIT HOOK] Executing automated pre-commit unit test verification...
Ran 31 tests in 0.001s

OK
✅ [GIT HOOK] All unit tests passed. Proceeding with commit.
[main 9f8e7d6] chore: test pre-commit hook with clean tests
 1 file changed, 1 insertion(+)
```
The hook verified the test suite and allowed the commit!

---

### Task 12.4: Test the Hook Blocking a Regression
Now let's intentionally introduce a broken calculation in `src/calculator.py`:

```python
def add(a: Number, b: Number) -> Number:
    # BUG: Accidental minus
    return a - b
```

Attempt to commit the broken code:
```powershell
git add src/calculator.py
git commit -m "refactor(calc): alter addition logic"
```

**Git stops execution and aborts the commit!**
```text
🔍 [GIT HOOK] Executing automated pre-commit unit test verification...
FAIL: test_add_integers (tests.test_calculator.TestCalculatorBasicOperations)
AssertionError: 5 != 15
❌ [GIT HOOK] Tests failed! Commit aborted to preserve repository integrity.
```

Check `git status`:
```powershell
git status
```
The commit was never created! The repository was protected from broken code.

Restore the pristine code:
```powershell
git restore src/calculator.py
```

Clean up the test commit:
```powershell
git reset --hard HEAD~1
```

---

### Task 12.5: The Emergency Bypass (`--no-verify`)
In rare situations where you must save work immediately despite broken tests:
```powershell
git commit -m "chore: emergency checkpoint" --no-verify
```
The `--no-verify` flag bypasses all client-side pre-commit hooks. Use with extreme discretion.

---

## 🔍 Verification Steps
1. Run `git status` — confirm clean working tree.
2. Run `python -m unittest discover tests` — all unit tests pass with `OK`.
3. Verify `.git/hooks/pre-commit` exists and is active.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| Hook does not execute | Script still has `.sample` extension or filename is misspelled. | Ensure file is named exactly `.git/hooks/pre-commit` (no extension). |
| Hook not shared when repository is cloned | `.git/hooks` is not tracked by Git for security reasons. | Store hooks in `.githooks/` in the repository and run `git config core.hooksPath .githooks/`. |
| Python not found in Git Bash/Sh runner | Python executable not in system PATH. | Ensure Python is added to Windows system environment PATH. |

---

## ✅ Completion Checklist
- [ ] Explored `.git/hooks/` directory.
- [ ] Authored an automated `pre-commit` hook executing Python `unittest`.
- [ ] Verified that passing tests allow commits.
- [ ] Verified that failing tests automatically block commits.
- [ ] Learned the emergency bypass flag (`--no-verify`).

