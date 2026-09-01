import pyautogui
import time

# Press the Windows/Super key
pyautogui.press("win")

# Type "text editor"
pyautogui.write("text editor", interval=0.1)

# Press Enter
pyautogui.press("enter")

# Wait for Text Editor to open
time.sleep(2)

# Now start typing
pyautogui.write("Hello! I am learning PyAutoGUI.", interval=0.05)
pyautogui.press("enter")
pyautogui.write("This text was typed automatically!")