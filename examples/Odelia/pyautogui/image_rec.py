'''import pyautogui
import time

pyautogui.FAILSAFE = True

print("Bot started...")

while True:

    button = pyautogui.locateOnScreen("button.png")

    if button:
        center = pyautogui.center(button)

        pyautogui.click(center)

        print("Button clicked!")
        break

    print("Waiting for button...")
    time.sleep(1)'''

from pathlib import Path
import pyautogui
import time

print("Move your mouse over the button you want to capture.")
print("You have 3 seconds...")

time.sleep(3)

x, y = pyautogui.position()

button_image = pyautogui.screenshot(
    region=(x - 75, y - 25, 150, 50)
)

# Save button.png in the same folder as this Python file
button_path = Path(__file__).parent / "button.png"

button_image.save(button_path)

print(f"button.png saved to: {button_path}")