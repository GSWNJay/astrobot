import pyautogui as pag
import time

pag.FAILSAFE = True

# Write automate text on terminal
pag.PAUSE = 1
print(pag.position())
pag.write("AstroBot_example here!! Typing an automated message ", interval=0.1)
pag.typewrite("Here's another way of automating writing", interval=0.1)

print("\nKeyboard keys available for use are: ")
print(pag.KEYBOARD_KEYS)

# Open Notepad/Text Editor and write a text in document
pag.press('win')
pag.PAUSE = 1.5
pag.write("Text", interval=0.1)
pag.PAUSE = 1.5
pag.press('enter')
time.sleep(30)

pag.typewrite("Automated Text by Astrobot on this document", interval=0.2)
pag.PAUSE = 3
pag.hotkey('ctrl', 'a') # Select all
pag.PAUSE = 1
pag.hotkey('ctrl', 'c') # Copy all the text from document to clipboard
pag.PAUSE = 1
pag.press('right')
pag.press('enter')
pag.PAUSE = 1
pag.hotkey('ctrl', 'v') # Paste the copied text 
#pag.hotkey('ctrl', 's') # Save the document