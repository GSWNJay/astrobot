import pyautogui
import time

# Get current position
x, y = pyautogui.position()
print(f"Mouse at: {x}, {y}")

pyautogui.PAUSE = 1

# Move mouse smoothly
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()
print(f"Mouse now at: {pyautogui.position()}")
