# Contributing to AstroBot

Danko contributors of AstroBot! This document provides guidelines for team collaboration. 

---

## 🌿 Branch Strategy

- **`main`** - Production-ready code (protected, only @GSWNJay can merge)
- **`develop`** - Active development (merge feature branches here)
- **`feature/*`** - New features (e.g., `feature/selenium-login`)
- **`fix/*`** - Bug fixes (e.g., `fix/scraper-timeout`)

---

## Workflow

### 1. Start a New Feature

```bash
# Make sure you're on develop and up-to-date
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Changes

```bash
# Make your changes, then stage and commit
git add .
git commit -m "Add descriptive commit message"

# Commit messages should be clear: 
# ✅ "Add login automation with Selenium"
# ✅ "Fix timeout error in web scraper"
# ❌ "Updated stuff"
# ❌ "Fix"
```

### 3. Push and Create Pull Request

```bash
# Push your branch
git push origin feature/your-feature-name
```

Then on GitHub:
1. Go to the repository
2. Click "Pull requests" → "New pull request"
3. Select `develop` as base and your feature branch
4. Add description of changes
5. Request review from @GSWNJay
6. Wait for approval before merging

---

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
<type>: <subject>

<optional body>
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code formatting (no logic change)
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

**Examples:**
```
feat: Add BeautifulSoup scraper for news headlines
fix: Handle timeout errors in Selenium driver
docs: Update LEARNING_PATH with PyAutoGUI examples
```

---

## Before Pushing

1. **Test your code** - Make sure it works! 
2. **Format your code** - Use Black or follow PEP 8
3. **No secrets** - Check for API keys, passwords
4. **Update docs** - If you add features, document them

---

## Rules

- ❌ Never push directly to `main`
- ❌ Never commit secrets/API keys
- ❌ Never force push to shared branches
- ✅ Always test before pushing
- ✅ Always create PRs for review
- ✅ Always write descriptive commits

---

## 🐛 Reporting Issues

Found a bug? Create an issue: 
1. Go to "Issues" tab
2. Click "New issue"
3. Describe the problem clearly
4. Include error messages if applicable
5. Add steps to reproduce

---

## Questions?

- Open an issue for discussion
- Ask in VS Code Copilot Chat Claude Sonnet (Preferrably, or any other Claude AI versions)
- Reach out via the group chat or @GSWNJay on GitHub

---

**LeT's BuRn ThIs CaNdLe 🚀**