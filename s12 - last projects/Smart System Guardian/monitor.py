import psutil
import os
import logging


logging.basicConfig(filename="guardian.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    return cpu_usage, ram_usage


def find_heavy_process():
    process = []
    for proc in psutil.process_iter(["pid", "name", "memory_percent"]):
        try:
            process.append(proc.info)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    heavy_process = max(process, key=lambda x: x["memory_percent"])
    return heavy_process


if __name__ == "__main__":
    cpu, ram = get_system_status()
    print(f"CPU: {cpu}% | RAM: {ram}%")
    print(f"Top process: {find_heavy_process()}")
