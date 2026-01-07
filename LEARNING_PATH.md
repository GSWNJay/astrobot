# AstroBot Learning Path

Here is our structured journey to building AstroBot.  With thi plan we should pull off this rocket science across all four main technologies.


## Phase 1: PyAutoGUI - Computer Automation

**Goal:** Control your computer programmatically

### Week 1: Basics

#### Day 1-2: Mouse Control
- [ ] Install PyAutoGUI
- [ ] Learn `pyautogui. position()` - get mouse position
- [ ] Learn `pyautogui.moveTo()` - move mouse
- [ ] Learn `pyautogui.click()` - click mouse
- [ ] **Exercise:** Create a script that moves mouse in a square pattern

**Example to try:**
```python
import pyautogui
import time

# Get current position
x, y = pyautogui. position()
print(f"Mouse at: {x}, {y}")

# Move mouse smoothly
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()
```

#### Day 3-4: Keyboard Control
- [ ] Learn `pyautogui.write()` - type text
- [ ] Learn `pyautogui.press()` - press keys
- [ ] Learn `pyautogui.hotkey()` - keyboard shortcuts
- [ ] **Exercise:** Automate opening Notepad and typing a message

#### Day 5-7: Screenshots & Image Recognition
- [ ] Learn `pyautogui.screenshot()` - capture screen
- [ ] Learn `pyautogui.locateOnScreen()` - find images
- [ ] **Project:** Build a simple bot that clicks a button when it appears

### Week 2: Mini-Project
- [ ] **Project:** Build a "Desktop Assistant" that: 
  - Opens applications on command
  - Types pre-defined messages
  - Takes screenshots at intervals

**Resources:**
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
- Place any samples in your `examples/pyautogui_examples/` as reference code

---