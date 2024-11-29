import os
import random


def generate_stats(stats, name, gender):
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
            "Power Erasure",
        ]

        dexterity = random.randint(0, 100)
        age = random.randint(0, 10000)

        numofabilities = int(
            input("How many extra abilities do you want? ")
        )
        os.system('clear')

        numofabilities = min(numofabilities, len(extraabilities))

        selected_abilities = random.sample(
            extraabilities, numofabilities
        )

        file.write("Name: " + name + "\n")
        file.write("Gender: " + gender + "\n")
        file.write("Strength: " + str(strength) + "\n")
        file.write("Magic: " + str(magic) + "\n")
        file.write("Dexterity: " + str(dexterity) + "\n")

        for ability in selected_abilities:
            file.write("Extra Ability: " + ability + "\n")


def main():
    print("Welcome to the RPG character/Pokemon stat creator")

    name1 = input("\nPlease put in the name of your first character:\n")
    gender1 = input("What gender is your first character? (Female or Male):\n")
    os.system('clear')
    generate_stats("Stat1", name1, gender1)

    name2 = input("\nPlease put in the name of your second character:\n")
    gender2 = input("What gender is your second character? (Female or Male):\n")

    generate_stats("Stat2", name2, gender2)

    print("\nStats have been successfully generated!")


main()
