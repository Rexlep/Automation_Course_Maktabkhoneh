tasks = ["numpy", "pandas", "matplotlib"]
log = []

for task in tasks:
    print(f"Task {task}")
    status = input("done? y or n: ")

    if status == "y":
        log.append((task, "done"))
    else:
        log.append((task, "failed"))


print("\nDaily Report")
for t, s in log:
    print(f"Task {t}, status {s}")