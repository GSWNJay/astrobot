import pyautogui 

x, y = pyautogui.position()
print(f"Mouse at: {x}, {y}")

# move from starting position 
pyautogui.moveTo(300, 300, duration=1)

pyautogui.moveTo(500, 300, duration=1)

pyautogui.moveTo(500, 500, duration=1)

pyautogui.moveTo(300, 500, duration=1)

pyautogui.moveTo(300, 300, duration=1)

pyautogui.click()