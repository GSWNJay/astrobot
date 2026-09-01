import pyautogui
import time
import math 

time.sleep(3)

# Starting position
start_x, start_y = pyautogui.position()

# =====================
# SQUARE
# =====================

size = 200

pyautogui.moveTo(start_x + size, start_y, duration=0.5)
pyautogui.moveTo(start_x + size, start_y + size, duration=0.5)
pyautogui.moveTo(start_x, start_y + size, duration=0.5)
pyautogui.moveTo(start_x, start_y, duration=0.5)

time.sleep(1)

# =====================
# CIRCLE
# =====================

radius = 100

for angle in range(0, 361, 5):
    radians = math.radians(angle)

    x = start_x + radius * math.cos(radians)
    y = start_y + radius * math.sin(radians)

    pyautogui.moveTo(x, y, duration=0.03)

'''# Get current position
x, y = pyautogui.position()
print(f"Mouse at: {x}, {y}")

# Move mouse smoothly
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()'''
