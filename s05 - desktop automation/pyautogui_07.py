import pyautogui

screen_shot = pyautogui.screenshot()
screen_shot.save("screen.png")

region = (100, 200, 700, 300)

screen_shot = pyautogui.screenshot(region=region)
screen_shot.save("screen_region.png")


pixel_color = pyautogui.pixel(1188, 359)
print(pixel_color)

if pyautogui.pixelMatchesColor(43, 491, (255, 0, 0)):
    print("This is red")
else:
    print("This is not red")