import pyautogui
import time

pyautogui.sleep(1)
time.sleep(1)

start_time = time.time()

for i in range(5):
    pyautogui.press("tab")

end_time = time.time()
print(f"Operation took {end_time - start_time:.2f} seconds")


def wait_for_image(image_path, timeout=10):
    start = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        if location:
            return location
        time.sleep(0.5)
    return None


wait_for_image("project.png", timeout=15)