def main():
    
    animals = ["Fox", "Fly", "Ant", "Bee", "Cod"]
    animals.append("Bear")
    animals2 = ["Goat"]
    animals.extend(animals2)
    animals.append(animals2)


    print(animals)

main()
