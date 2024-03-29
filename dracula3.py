

with open("dracula.txt", "r") as drac:
    for line in drac:
        if "vampire" in line.lower():
            print(line)