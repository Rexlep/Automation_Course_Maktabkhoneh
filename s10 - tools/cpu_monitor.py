import psutil

print("CPU: ", psutil.cpu_percent(interval=1), "%")
print(psutil.cpu_count(logical=True))

print(psutil.cpu_percent(interval=1, percpu=True))