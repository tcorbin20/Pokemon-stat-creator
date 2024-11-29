import os
import random

def generate_stats(stats, name):
    with open(stats, "w") as file:

        strength = random.randint(0, 100)
        magic = random.randint(0, 100)
        extraabilities = [
            "Aquatic Breathing",
            "Mental Projection",
            "Healing",
            "Power Erasure",
            "Astral Vision",
            "Camouflage",
            "Psychic Constructs",
            "Superpower Manipulation",
            "Acid Generation",
            "Power Erasure"
        ]

        dexterity = random.randint(0, 100)
        age = random.randint(0, 10000)


        file.write("Your stats are as follows:\n")
        file.write("Name: " +name + "\n")
        file.write("Gender:" +gender + "\n")
        file.write("Strength: " +str(strength) + "\n")
        file.write("Magic: " + str(magic) + "\n")
        file.write("Dexterity: " + str(dexterity) + "\n")
        
        randomabilities1 = random.choice(extraabilities)
        file.write("Extra Ability: " + randomabilities1 + "\n")

def main():
    print("Welcome to the RPG character/Pokemon stat creator")


    name1 = input("\nPlease put in the name of your first character:\n")
    

    generate_stats("Stat1.txt", name1)
    

    name2 = input("\nPlease put in the name of your second character:\n")
    
    generate_stats("Stat2.txt", name2)

    gender1 = input("What gender is your first character: Female or Male\n")
    generate_stats("Stat1.txt",gender1)
    gender2 = input("What gender is your second character: Female or Male\n")
    generate_stats("Stat1.txt",gender2)
    print("\nStats have been successfully generated!")

main()
