import pyautogui
import subprocess
import time

subprocess.Popen(["open", "-a", "TextEdit"])

time.sleep(2)

pyautogui.write("Hello Odelia and Njabulo!")
pyautogui.press("Enter")

#keyboard shortcuts
pyautogui.hotkey("command", "a")
