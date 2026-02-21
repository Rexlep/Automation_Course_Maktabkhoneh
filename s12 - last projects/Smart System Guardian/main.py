import time
from monitor import get_system_status, find_heavy_process
from action import take_alert_screenshot, kill_process

CPU_THRESHOLD = 80.0
RAM_THRESHOLD = 80.0


def start_guardian():
    print("System guardian is running")
    while True:
        cpu, ram = get_system_status()

        if cpu > CPU_THRESHOLD or ram > RAM_THRESHOLD:
            print(f"Alert High Usage detected: cpu: {cpu}% ram: {ram}%")

            screenshot_file = take_alert_screenshot()

            target = find_heavy_process()
            print(f"Terminating heavy process: {target['name']} (PID: {target['pid']})")

            success = kill_process(target['pid'])

            if success:
                print(f"Successfully Killed {target['name']}. screenshot saved")

        time.sleep(5)


if __name__ == "__main__":
    start_guardian()