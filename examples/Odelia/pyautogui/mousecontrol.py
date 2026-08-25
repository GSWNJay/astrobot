import pyautogui
import time

# Get current position
x, y = pyautogui.position()
print(f"Mouse at: {x}, {y}")

# Move mouse smoothly
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()
