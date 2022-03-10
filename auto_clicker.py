import pyautogui as p
import time

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
time.sleep(1)

while True:
    p.click(640, 530)

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
