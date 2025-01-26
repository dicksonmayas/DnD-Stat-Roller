import random
import math


class Character:
    class Stat:
        def __init__(self, name: str):
            self.name = name
            self.score = 0
            self.modifier = 0

    # List of stat names
    def __init__(self):
        self.stats = [
            self.Stat("STR"),
            self.Stat("DEX"),
            self.Stat("CON"),
            self.Stat("INT"),
            self.Stat("WIS"),
            self.Stat("CHA")
        ]
        self.num_rolls = self.get_user_choice()
        self.roll_stats()

    # Function to integrate with roll_stat()
    def get_user_choice(self) -> int:
        while True:
            try:
                choice = int(input("Choose rolling method:\n1. Roll 3d6"
                                   "\n2. Roll 4d6 drop lowest\nEnter choice (1/2): "))

                # Catches choices outside the range
                if choice in (1, 2):
                    return 3 if choice == 1 else 4
                print("Please enter 1 or 2.")

            except ValueError:
                print("Please enter a number.")

    # Function to roll 3d6 or 4d6 drop lowest
    def roll_stat(self, num_rolls: int) -> int:
        # Roll d6s per the given parameter
        rolls = [random.randint(1, 6) for _ in range(num_rolls)]

        # Sorts the list
        rolls.sort()

        # Returns the sum of the highest rolls in case of 4d6
        return sum(rolls[-3:])

    # Function to calculate the stat modifiers
    def calculate_modifier(self, score: int) -> int:
        return math.floor((score - 10) / 2)

    # Function to assign constructor values to function calls
    def roll_stats(self):
        for stat in self.stats:
            stat.score = self.roll_stat(self.num_rolls)
            stat.modifier = self.calculate_modifier(stat.score)

    # Function to display stat name pairs with stat total and corresponding modifier
    def display_stats(self):
        print("\nDnD Character Stats:"
              "\n____________________\n")
        for stat in self.stats:
            print(f"{stat.name}: {stat.score} ({'+' if stat.modifier >= 0 else ''}{stat.modifier})")


# Function to initialize class object
def main():

    # RNG seed
    random.seed()
    my_char = Character()
    my_char.display_stats()


# Runs class object
if __name__ == "__main__":
    main()




