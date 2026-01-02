# 🤖 AstroBot (ABot)

**An AI-powered automation bot built with Python to learn and master:**
- 🖱️ **PyAutoGUI** - Computer automation
- 🌐 **BeautifulSoup** - Web scraping
- 🤖 **Selenium** - Browser automation
- 🧠 **GitHub Copilot API** - AI integration

> **Status:** 🚧 In Development - Learning Project  
> **Started:** 2025-12-22

---

## Project Goals

This is a **learning-focused project** designed to: 
1. Master Python automation libraries
2. Build a modular, extensible bot framework
3. Integrate AI capabilities via GitHub Copilot API
4. Practice collaborative development with Git workflows

---

## Project Structure

```
AstroBot/
├── modules/                    # Core bot modules
│   ├── pyautogui_module/      # Computer automation
│   ├── scraping_module/       # Web scraping with BeautifulSoup
│   ├── selenium_module/       # Browser automation
│   └── copilot_module/        # GitHub Copilot API integration
├── examples/                   # Learning examples for each module
├── tests/                      # Unit tests
├── docs/                       # Documentation
├── .github/workflows/          # CI/CD workflows
├── requirements.txt            # Python dependencies
└── LEARNING_PATH.md            # Step-by-step learning guide
```

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git installed
- GitHub account

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GSWNJay/AstroBot.git
   cd AstroBot
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Activate (Windows)
   venv\Scripts\activate
   
   # Activate (Mac/Linux)
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start learning! **
   Check out `LEARNING_PATH.md` for the structured learning roadmap.

---

## 👥 Team

- **Project Lead:** [@GSWNJay](https://github.com/GSWNJay)
- **Developers:** 
  - [@MinnieNtontela](https://github.com/MinnieNtontela)
  - [@AyandaEnhle](https://github.com/AyandaEnhle)

---

## 🌿 Branch Strategy

- `main` - Protected branch (only @GSWNJay can merge)
- `develop` - Active development branch
- `feature/*` - Feature branches
- `fix/*` - Bug fix branches

**Workflow:**
1. Create feature branch from `develop`
2. Make changes and commit
3. Push to GitHub
4. Create Pull Request to `develop`
5. After review, merge to `develop`
6. @GSWNJay merges `develop` to `main`

---

## 📚 Learning Roadmap (Subject to change)

### Phase 1: PyAutoGUI (Computer Automation)
- [ ] Mouse control
- [ ] Keyboard automation
- [ ] Screenshot capabilities
- [ ] GUI automation basics

### Phase 2: BeautifulSoup (Web Scraping)
- [ ] HTML parsing
- [ ] Data extraction
- [ ] Navigate website structures
- [ ] Handle different HTML elements

### Phase 3: Selenium (Browser Automation)
- [ ] WebDriver setup
- [ ] Browser navigation
- [ ] Form filling
- [ ] Element interaction
- [ ] Headless browsing

### Phase 4: GitHub Copilot API
- [ ] API authentication
- [ ] Request/response handling
- [ ] Integrate AI suggestions
- [ ] Build AI-powered features

### Phase 5: Integration
- [ ] Combine all modules
- [ ] Build AstroBot core
- [ ] Error handling
- [ ] Logging system
- [ ] Task scheduling

---

## 🔒 Security

This is a **public repository** during development in order to allow branch protection rules.

**Important:**
- Never commit API keys or credentials
- Use `.env` files for sensitive data
- Review `.gitignore` before committing

---

## License

MIT License

---

## Contributors

For team members:
1. Always work on feature branches
2. Write descriptive commit messages
3. Test your code before pushing
4. Create PRs for code review
5. Follow Python best practices (PEP 8)

---

**Let's build something amazing!  🚀**