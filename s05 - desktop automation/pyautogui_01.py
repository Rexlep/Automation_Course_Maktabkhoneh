import pyautogui

print(pyautogui.__version__)
print(f"Screen size {pyautogui.size()}")

width, height = pyautogui.size()
print(width, height)

print(pyautogui.position())
x, y = pyautogui.position()
print(x, y)