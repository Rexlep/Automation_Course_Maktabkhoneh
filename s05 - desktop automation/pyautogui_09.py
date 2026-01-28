import pyautogui
import time

active_window = pyautogui.getActiveWindow()

if active_window:
    print(active_window.title)
    print(active_window.size)
    print(active_window.topleft)
    print(active_window.minimize)


windows = pyautogui.getAllWindows()
for window in windows:
    if window.title:
        print(window.title)


firefox_window = pyautogui.getWindowsWithTitle("Mozilla Firefox")
if firefox_window:
    firefox = firefox_window[0]

    firefox.activate()
    time.sleep(1)

    firefox.maximize()
    time.sleep(1)

    firefox.restore()
    time.sleep(1)