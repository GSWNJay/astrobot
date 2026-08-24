import pyautogui as pag
import time

# Get current position
x, y = pag.position()
print(f"Mouse at: {x}, {y}")

pag.PAUSE = 1

# Move mouse smoothly
pag.moveTo(100, 100, duration=1)
# pag.click()
print(f"Mouse now at: {pag.position()}")

pag.FAILSAFE = True
pag.PAUSE = 1

# Draw a square with mouse
pixels = 200

if(not pag.onScreen(pag.position().x + pixels, pag.position().y + pixels)):
    print("Mouse is too close to the edge of the screen, let me move it to a crash free zone for you sir.")
    pag.moveTo(500, 500, duration=1)

pag.moveRel(pixels, 0, duration=0.5) # →
pag.moveRel(0, pixels, duration=0.5) # ↓
pag.moveRel(-pixels, 0, duration=0.5) # ←
pag.moveRel(0, -pixels, duration=0.5) # ↑


