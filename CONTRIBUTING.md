# 🤝 Contributing to Git & GitHub Demonstration Project

Welcome! We are excited to collaborate with you. Whether you are adding a new robotics telemetry utility, reporting a bug, or polishing documentation, this guide details our development standards and contribution lifecycle.

---

## 📜 Code of Conduct

We are committed to fostering an inclusive, welcoming, and harassment-free engineering community. All contributors, maintainers, and reviewers are expected to treat peers with mutual respect, patience, and empathy.

---

## 🛠 Local Development Setup

### 1. Prerequisites
- Python 3.8 or higher (`python --version`)
- Git 2.23 or higher (`git --version`)

### 2. Fork and Clone
```bash
# Clone the repository
git clone https://github.com/<your-username>/Git_GitHub_Week03.git
cd Git_GitHub_Week03
```

### 3. Initialize Virtual Environment (Recommended)
```bash
# On Windows PowerShell / Command Prompt:
python -m venv .venv
.venv\Scripts\activate

# On macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
```

---

## 🌿 Contribution Workflow

Always adhere to the isolated topic branch workflow:

### Step 1: Create a Topic Branch
Ensure your local `main` is up-to-date with upstream:
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```
*(Branch naming convention: `feature/*`, `fix/*`, `docs/*`, `test/*`, `refactor/*`)*

### Step 2: Implement Your Changes
- Maintain documentation integrity and preserve existing docstrings.
- Ensure strict type hints (`typing` module) and clear variable naming.
- Keep functions pure and modular whenever possible.

### Step 3: Run the Test Suite
**All tests must pass** prior to staging:
```bash
python -m unittest discover tests
```

To run individual test files:
```bash
python tests/test_calculator.py
python tests/test_greeting.py
```

### Step 4: Follow Conventional Commits
Write clean, atomic commit messages following the Conventional Commits format:
```bash
git add src/calculator.py tests/test_calculator.py
git commit -m "feat(calc): add rolling standard deviation for sensor filtering"
```

### Step 5: Push and Open a Pull Request
```bash
git push -u origin feature/your-feature-name
```
Navigate to your repository on GitHub and open a Pull Request. Complete all items in the automated PR Checklist template.

---

## 🎨 Code Style and Formatting Standards

- **PEP 8**: Follow standard Python style conventions (4-space indentation, snake_case for functions and variables, PascalCase for classes).
- **Docstrings**: Provide Google-style docstrings with `Args:`, `Returns:`, and `Raises:` blocks.
- **Type Annotations**: Annotate all public function parameters and return types.
- **Error Handling**: Use specific exceptions (`TypeError`, `ValueError`, `ZeroDivisionError`) with actionable error messages.

---

## ❓ Need Assistance?

If you have questions or encounter blockers during your practice lab, open an issue using the appropriate template or start a discussion thread. Happy engineering!

