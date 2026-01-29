import pyautogui
import random
import time
import webbrowser


def human_move(x, y, duration=1):
    start_x, start_y = pyautogui.position()
    steps = random.randint(20, 40)

    for i in range(steps):
        t = i / steps
        cur_x = start_x + (x - start_x) * t + random.uniform(-3, 3)
        cur_y = start_y + (y - start_y) * t + random.uniform(-3, 3)

        pyautogui.moveTo(cur_x, cur_y)
        time.sleep(duration / steps)


def human_type(text):
    for ch in text:
        if random.random() < 0.05:

            pyautogui.write(random.choice("asdfghjkl"))
            pyautogui.press("backspace")

        pyautogui.write(ch)
        time.sleep(random.uniform(0.05, 0.25))


def human_pause():
    time.sleep(random.uniform(0.5, 2))


def scenario():
    webbrowser.open("https://www.google.com")

    search_box_x, search_box_y = 941, 530

    time.sleep(2)

    human_move(search_box_x, search_box_y)

    pyautogui.click()
    human_pause()

    human_type("Maktabkhoone")
    human_pause()
    pyautogui.press("enter")


print("Starting the program")
time.sleep(2)
scenario()