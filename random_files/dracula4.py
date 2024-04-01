

with open("dracula.txt", "r") as drac:
    vampire_count = 0
    for line in drac:
        if "vampire" in line.lower():
            vampire_count += 1
print(vampire_count)
