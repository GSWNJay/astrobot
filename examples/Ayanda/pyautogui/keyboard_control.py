import pyautogui
import time

# Open Spotlight
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")

time.sleep(2)
pyautogui.write("TextEdit")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("Hello Odelia and Njabulo!")
pyautogui.press("enter")
pyautogui.write("Ninjani")

pyautogui.keyDown("command")
pyautogui.press("a")
pyautogui.keyUp("command")