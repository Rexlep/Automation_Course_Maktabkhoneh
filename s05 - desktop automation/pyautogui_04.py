import pyautogui
import time


time.sleep(2)

pyautogui.moveTo(136, 166)
pyautogui.mouseDown(button="left")
pyautogui.dragTo(500, 0, button='left')
