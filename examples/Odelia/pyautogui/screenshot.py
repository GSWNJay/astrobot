'''import pyautogui
import time

time.sleep(2)

screenshot = pyautogui.screenshot() #can add region=(0,0, 300, 400) to limit the area of the screenshot

screenshot.save("my_screen.png")

print("Screenshot saved!")


import pyautogui
import time

print("Move your mouse over the button you want to capture.")
print("You have 3 seconds...")

time.sleep(3)

# Get the current mouse position
x, y = pyautogui.position()

# Capture a 150x50 area around the mouse
button_image = pyautogui.screenshot(
    region=(x - 75, y - 25, 150, 50)
)

# Save it as button.png
button_image.save("button.png")

print("button.png created!")'''


from pathlib import Path
import pyautogui
import time

time.sleep(2)

screenshot = pyautogui.screenshot()

# Save screenshot in the same folder as this Python file
screenshot_path = Path(__file__).parent / "screenshot.png"

screenshot.save(screenshot_path)

print(f"Screenshot saved to: {screenshot_path}")