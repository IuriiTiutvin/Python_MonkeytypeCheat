import pyautogui as g
import time

g.FAILSAFE = True

for i in range(500):
    time.sleep(0.8)
    g.click(500, 750)
    g.write('Get on Apex')
    g.press('enter')
