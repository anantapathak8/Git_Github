# 🏷️ Lab 10: Semantic Versioning, Git Tags & GitHub Releases

> **Objective**: Understand Semantic Versioning (SemVer); distinguish between lightweight and annotated tags; create, verify, and push release tags; and publish an official GitHub Release.

---

## 📋 Prerequisites
1. Completion of Lab 09.
2. Clean working tree on `main` in `Git_GitHub_Week03`.
3. Test suite passing (`python -m unittest discover tests`).

---

## 📖 Theoretical Context: Semantic Versioning & Tags

In engineering software distributions (such as ROS2 robot packages or PyPI libraries), version numbers communicate compatibility:

### Semantic Versioning Specification (`MAJOR.MINOR.PATCH`):
Given a version number `X.Y.Z`:
1. **MAJOR (X)**: Incremented when making incompatible API breaking changes.
2. **MINOR (Y)**: Incremented when adding functionality in a backwards-compatible manner.
3. **PATCH (Z)**: Incremented when making backwards-compatible bug fixes.

### Lightweight vs Annotated Tags:
- **Lightweight Tag**: A simple bookmark pointing directly to a commit hash. No author or date metadata.
- **Annotated Tag**: A full Git object stored in `.git/objects/`. Includes the creator's name, email, date stamp, a custom release message, and optional GPG cryptographic signatures. **Always use annotated tags for public releases.**

---

## 💻 Step-by-Step Instructions & Exact Commands

### Task 10.1: Create an Annotated Release Tag
Ensure you are on `main` and working tree is clean:

```powershell
git switch main
git status
```

Create an annotated tag for version 1.0.0:
```powershell
git tag -a v1.0.0 -m "Release v1.0.0: Foundation release with arithmetic, telemetry, greeting modules and unit test suite"
```

Verify the tag was created:
```powershell
git tag
```

**Expected Output:**
```text
v1.0.0
```

---

### Task 10.2: Inspect Tag Metadata
Inspect the tag object using `git show`:

```powershell
git show v1.0.0
```

**Expected Output:**
```text
tag v1.0.0
Tagger: Your Name <your.email@university.edu>
Date:   Mon Nov 9 18:50:00 2026 +0530

Release v1.0.0: Foundation release with arithmetic, telemetry, greeting modules and unit test suite

commit 9d4e12a... (tag: v1.0.0, main)
Author: Your Name <your.email@university.edu>
...
```

Notice the explicit `Tagger` and `Date` fields separate from the commit author!

---

### Task 10.3: Tagging Historical Commits
Suppose you forgot to tag a previous milestone (e.g., prototype version `v0.1.0`):

Find the commit hash:
```powershell
git log --reverse --oneline
# Example: 9d4e12a
```

Apply an annotated tag to that specific past commit:
```powershell
git tag -a v0.1.0 9d4e12a -m "Release v0.1.0: Initial prototype setup"
```

Filter tags by pattern:
```powershell
git tag -l "v1.*"
```

---

### Task 10.4: Pushing Tags to GitHub
By default, `git push` does **not** push tags to remote servers! You must push tags explicitly:

```powershell
# Push a specific tag
git push origin v1.0.0

# Push all local tags simultaneously
git push origin --tags
```

---

### Task 10.5: Publishing an Official GitHub Release

Once the tag is pushed to GitHub:

1. Navigate to your repository on GitHub.
2. In the right-hand sidebar, click **Releases**.
3. Click **Draft a new release**.
4. Select tag `v1.0.0`.
5. Set Release Title: `v1.0.0 — Stable Foundation Release`.
6. Click **Generate release notes** (GitHub automatically aggregates merged PR titles).
7. Paste relevant excerpts from `CHANGELOG.md`.
8. Click **Publish release**.

GitHub automatically bundles source code archives (`.zip` and `.tar.gz`) for users to download!

---

### Task 10.6: Deleting Tags Safely
If a tag was created erroneously:

```powershell
# Delete tag locally
git tag -d v0.1.0

# Delete tag on remote (GitHub)
git push origin --delete v0.1.0
```

---

## 🔍 Verification Steps
1. Run `git tag -n` — list all tags alongside their release notes.
2. Run `git describe --tags` — outputs `v1.0.0`.
3. Open GitHub Releases page — confirm release notes and source archives are published.

---

## ⚠️ Common Mistakes and Solutions

| Mistake / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| Tags missing on GitHub after `git push` | Standard `git push` does not include tags. | Run `git push origin --tags` or specify tag name. |
| Created lightweight tag instead of annotated | Omitted `-a` and `-m` flags. | Delete with `git tag -d <tag>` and recreate with `git tag -a <tag> -m "..."`. |
| Tag names don't follow SemVer | Missing `v` prefix or invalid version format. | Follow `vMAJOR.MINOR.PATCH` convention (e.g., `v1.0.0`). |

---

## ✅ Completion Checklist
- [ ] Created an annotated release tag (`git tag -a v1.0.0`).
- [ ] Inspected tagger metadata using `git show`.
- [ ] Tagged a past commit by hash.
- [ ] Pushed tags to GitHub with `git push origin --tags`.
- [ ] Drafted and published an official GitHub Release.
