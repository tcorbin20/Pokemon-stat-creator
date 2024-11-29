import os
import random
file = open("Stat","w")
file = open("Stat2", "w")
print("Welcome to the RPG character/Pokemon stat creator")


name1 = input("\nPlease put in the name of your character:\n")
def cardgenerator():
    gender = input("\nWhat gender is your character?: Female or Male")
    if gender == "Male" or gender == "Female" or gender == "male" or gender == "female":
        print("\n")
    else:
        print("\nInvalid")
        exit()

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
    "Power Erasure",
]
dexterity = random.randint(0, 100)
age = random.randint(0, 10000)
file.write("Your stats are as follows:")
file.write("\nName:")
file.write(name1)
file.write("\nStrength:")
file.write(str(strength))
file.write("\nMagic: ")
file.write(str(magic))
file.write("\nDexterity:")
file.write(str(dexterity))
randomabilities1 = random.choice(extraabilities)
file.write("\nExtra Abilitys:\n")
file.write(randomabilities1)
file.close
os.system("clear")
cardgenerator.exit


cardgenerator()

