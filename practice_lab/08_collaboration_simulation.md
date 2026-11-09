# 👥 Lab 08: Multi-Developer Collaboration Simulation

> **Objective**: Simulate a multi-engineer team on a single workstation by spinning up independent local repository clones with distinct developer identities (Alice: Robotics Engineer & Bob: AI Researcher), experiencing authentic push collisions and concurrent synchronization.

---

## 📋 Prerequisites
1. Completion of Lab 07.
2. Clean working tree on `main` in `Git_GitHub_Week03`.
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Why Simulate Team Collaboration?

Many engineers struggle when joining engineering teams because they only ever work alone. They are suddenly confronted with:
- Remote push rejections (`[rejected - non-fast-forward]`).
- Teammates modifying shared code while they were working.
- Needing to pull and rebase before pushing.

By simulating two developers (**Alice** and **Bob**) on your local machine using a local bare repository as the central hub, you will experience full collaborative dynamics without needing a second computer!

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 8.1: Create a Central Bare Repository
A **bare repository** has no working directory; it consists solely of `.git` administrative files and acts as the central server (just like GitHub!).

In PowerShell at repository root:
```powershell
# Create a sandbox directory (excluded by .gitignore)
New-Item -ItemType Directory -Path "practice_lab/sandbox" -Force

# Initialize a central bare repository cloned from current repo
git clone --bare . practice_lab/sandbox/central.git
```

---

### Task 8.2: Spawn Developer Clones (Alice & Bob)

Clone the central repository into two separate folders representing Alice and Bob's workstations:

```powershell
# Clone for Alice (Robotics Engineer)
git clone practice_lab/sandbox/central.git practice_lab/sandbox/alice_repo

# Clone for Bob (AI Specialist)
git clone practice_lab/sandbox/central.git practice_lab/sandbox/bob_repo
```

Configure independent identities for each clone:

```powershell
# Configure Alice's local identity
Set-Location practice_lab/sandbox/alice_repo
git config user.name "Alice Rover"
git config user.email "alice.rover@robotics.lab"

# Configure Bob's local identity
Set-Location ../bob_repo
git config user.name "Bob Neural"
git config user.email "bob.neural@ai.lab"

# Return to sandbox root
Set-Location ../../..
```

---

### Task 8.3: Alice Develops & Pushes a Feature

Navigate to Alice's workspace:
```powershell
Set-Location practice_lab/sandbox/alice_repo
git switch -c feature/alice-battery-monitor
```

Add a battery monitoring helper in `src/calculator.py`:
```python
def battery_percentage(voltage: Number, min_voltage: float = 9.6, max_voltage: float = 12.6) -> float:
    """Calculate remaining battery percentage for robotic power management."""
    _validate_numeric(voltage, "Voltage")
    if voltage <= min_voltage:
        return 0.0
    if voltage >= max_voltage:
        return 100.0
    return ((voltage - min_voltage) / (max_voltage - min_voltage)) * 100.0
```

Commit and push from Alice's machine:
```powershell
git add src/calculator.py
git commit -m "feat(power): implement battery percentage calculator for rover"
git switch main
git merge feature/alice-battery-monitor
git push origin main
```
Alice's commit is now published to `central.git`!

---

### Task 8.4: Bob Works Concurrently (The Collision)

Now switch over to Bob's machine:
```powershell
Set-Location ../bob_repo
```
*Notice Bob has NOT pulled Alice's changes yet. Bob is working on an older commit snapshot!*

Bob edits `src/greeting.py` to add an AI assistant utility:
```python
def ai_assistant_status(model_name: str = "Gemini-Robotics") -> str:
    """Return status string for onboard AI copilot."""
    return f"[AI COPILOT: {model_name}] Inference engine online and streaming."
```

Bob commits:
```powershell
git add src/greeting.py
git commit -m "feat(ai): add ai_assistant_status banner utility"
```

Now Bob attempts to push to `central.git`:
```powershell
git push origin main
```

**Git rejects Bob's push!**
```text
To practice_lab/sandbox/central.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'practice_lab/sandbox/central.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

---

### Task 8.5: Bob Resolves Synchronization with Rebase

Bob pulls Alice's changes and rebases his work cleanly on top:

```powershell
git pull --rebase origin main
```

**Expected Output:**
```text
Current branch main is up to date.
Applying: feat(ai): add ai_assistant_status banner utility
```
Because Alice edited `calculator.py` and Bob edited `greeting.py`, Git re-applies Bob's commit smoothly on top of Alice's latest commit!

Now Bob pushes cleanly:
```powershell
git push origin main
```
Push succeeds!

---

### Task 8.6: Inspecting the Collaborative Graph
Check the commit log inside Bob's repo:
```powershell
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' -n 5
```

Notice the author attribution:
- Alice's commit is authored by `Alice Rover <alice.rover@robotics.lab>`
- Bob's commit is authored by `Bob Neural <bob.neural@ai.lab>`

---

### Task 8.7: Synchronize Main Repository & Cleanup
Return to the primary repository root:
```powershell
Set-Location ../../..

# Pull the collaborative changes into your primary workspace
git pull practice_lab/sandbox/central.git main

# Run tests to confirm full system integrity
python -m unittest discover tests

# Clean up temporary simulation sandbox
Remove-Item -Recurse -Force practice_lab/sandbox
```

---

## 🔍 Verification Steps
1. Run `git log -n 5` — verify that both Alice's and Bob's commits appear in permanent history with distinct author emails.
2. Run `python -m unittest discover tests` — all unit tests pass with `OK`.
3. Run `Test-Path practice_lab/sandbox` — returns `False`, confirming sandbox cleanup.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `fatal: Not a valid object name` when creating bare clone | Repo had zero commits. | Complete Lab 01 (initial commit) before cloning bare repository. |
| Forgetting to use `Set-Location ../../..` | Executing commands in wrong clone directory. | Check active path with `Get-Location` (`pwd`). |
| Sandbox files appearing in `git status` | Sandbox path not ignored. | Verify `practice_lab/sandbox/` exists in `.gitignore`. |

---

## ✅ Completion Checklist
- [ ] Created a central bare repository (`central.git`).
- [ ] Created two distinct clones with independent identities (Alice & Bob).
- [ ] Pushed a feature from Alice to central.
- [ ] Simulated a non-fast-forward push rejection from Bob.
- [ ] Resolved concurrent sync using `git pull --rebase`.
- [ ] Pulled collaborative history into main repository and removed sandbox.
