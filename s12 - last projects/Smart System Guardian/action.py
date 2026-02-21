import psutil
import pyautogui
import datetime


def take_alert_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y%m%d - %H:%M:%S")
    filename = f"alert_screenshot_{timestamp}.png"

    pyautogui.screenshot(filename)
    return filename


def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        return True

    except Exception as e:
        print(f"Failed to kill process: {e}")
        return False