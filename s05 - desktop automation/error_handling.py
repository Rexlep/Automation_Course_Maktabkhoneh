import pyautogui
import sys

try:
    pyautogui.FAILSAFE = True

    pyautogui.PAUSE = 0.5

    pyautogui.moveTo(-10, -10)

except pyautogui.FailSafeException:
    print("Failsafe exception we try to move the cursor to the corner")
    sys.exit(0)

except Exception as e:
    print("Error:", e)

    with open("error_log.txt",  "a+") as f:
        import traceback
        traceback.print_exc(file=f)