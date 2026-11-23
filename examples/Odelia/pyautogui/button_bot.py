'''from pathlib import Path
import pyautogui
import time

print("AstroBot started...")

button_path = Path(_file_).parent / "button.png"

print(f"Looking for:{button_path}")

while True:
    try:
        button = pyautogui.locateOnScreen("button.png" ,confidence=0.8)  # Adjust confidence as needed  

        if button:
            print("Button found!")

            center = pyautogui.center(button)

            print(f"Button position: {center}")

            pyautogui.click(center)

            print("Button clicked!")
            break

    except pyautogui.ImageNotFoundException:
        print("Button not found... checking again")

    time.sleep(1)'''

from pathlib import Path
import pyautogui
import time

print("AstroBot started!")

# Find button.png in the same folder as this script
button_path = Path(__file__).parent / "button.png"

print(f"Looking for: {button_path}")

while True:
    try:
        button = pyautogui.locateOnScreen(str(button_path),confidence=0.6)

        if button:
            print("Button found!")

            center = pyautogui.center(button)
            print(f"Button location: {center}")

            pyautogui.click(center)

            print("Button clicked!")
            break

    except pyautogui.ImageNotFoundException:
        print("Button not found... checking again")

    time.sleep(1)
