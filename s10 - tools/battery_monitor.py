import psutil

battery = psutil.sensors_battery()

print(battery.percent)
print(battery.power_plugged)
