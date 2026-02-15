import psutil

ram = psutil.virtual_memory().percent
print(ram / (1024 ** 3))


print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)