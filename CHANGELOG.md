# 📋 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]
### Planned
- Matrix and vector transformations module in `src/kinematics.py` for robotic manipulator calculations.
- GitHub Actions CI/CD workflow running automated unittest matrix on Python 3.9, 3.10, 3.11, 3.12.
- Pre-commit hooks for automated Ruff linting and formatting.

---

## [1.0.0] - 2026-11-09
### Added
- **Core Calculator Module (`src/calculator.py`)**:
  - Arithmetic operations: addition, subtraction, multiplication, division.
  - Scientific & Robotics utilities: power (`power`), square root (`square_root`), arithmetic mean (`calculate_mean`).
  - Strict numeric validation with descriptive `TypeError`, `ValueError`, and `ZeroDivisionError` handling.
- **Greeting Module (`src/greeting.py`)**:
  - Configurable styles: `standard`, `formal`, `casual`, `robotics`, `developer`.
  - Time-aware greeting (`get_time_based_greeting`) handling morning, afternoon, evening, and night owl scenarios.
  - Terminal banner generator (`format_multiline_banner`).
- **Comprehensive Unit Test Suites (`tests/`)**:
  - `tests/test_calculator.py`: 16 comprehensive tests covering normal flow, edge cases, floats, zero-division, and negative boundaries.
  - `tests/test_greeting.py`: 12 comprehensive tests validating styles, time boundaries, string sanitization, and invalid inputs.
- **Git & GitHub Engineering Documentation**:
  - `GIT_WORKFLOW.md`: Complete guide on Git architectures, branching models (Git Flow vs GitHub Flow vs Trunk-Based), Conventional Commits, and Golden Rules.
  - `BRANCHING_EXERCISE.md`: Hands-on parallel branch simulation and lifecycle guide.
  - `MERGE_CONFLICT_GUIDE.md`: Deep dive on conflict markers, intentional collision reproduction, CLI resolution, and prevention.
  - `PULL_REQUEST_GUIDE.md`: Professional PR anatomy, review guidelines, upstream synchronization, and GitHub CLI tips.
  - `CONTRIBUTING.md`: Open-source contribution guidelines and PEP 8 standards.
- **GitHub Templates (`.github/`)**:
  - `.github/PULL_REQUEST_TEMPLATE.md`: Standardized pre-merge checklist and change summary.
  - `.github/ISSUE_TEMPLATE/bug_report.md`: Bug reporting schema.
  - `.github/ISSUE_TEMPLATE/feature_request.md`: Structured feature proposal template.
- **Practice Lab Modules (`practice_lab/`)**:
  - 10 structured, progressive hands-on lab modules from repository setup to tags & releases.
  - `CHALLENGE_CHECKLIST.md`: 30-item practical mastery checklist.

