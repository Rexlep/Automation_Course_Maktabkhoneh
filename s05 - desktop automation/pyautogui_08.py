import pyautogui

project_part = pyautogui.locateOnScreen('windo.png')

if project_part:
    print('Founded')
    center = pyautogui.center(project_part)
    pyautogui.click(center)

else:
    print('Not Found')