import pyautogui

pyautogui.moveTo(x=300, y=300, duration=2)

pyautogui.move(300, 300, duration=2)
print(pyautogui.position())
pyautogui.move(-300, -300)
print(pyautogui.position())
