import time
import random

enemies = ["Troll", "Dragon", "Witch", "Ghoul", "Alien"]
weapons = ["Sword", "Dagger", "Crossbow", "Pistol", "Flamethrower"]


enemy = random.choice(enemies)
weapon = random.choice(weapons)


def main():
    intro(enemy, weapon)
    act_I()


def intro(enemy, weapon):
    print_pause(
        "You find yourself standing in an open field, filled with grass and yellow wildflowers.",
        2,
    )
    print_pause(
        f"Rumor has it that a {enemy} is somewhere arounf here and has been terrifying the nearby village",
        2,
    )
    print_pause("In front of you is a house", 2)
    print_pause("to your right is a dark cave", 2)
    print_pause(f"in your hand you hold a rusty not so much effective {weapon}", 2)


def print_pause(message, num):
    print(message)
    time.sleep(num)


def fight():
    print_pause(
        f"you hold your weapon and swing it with great might to the {enemy} 's head", 2
    )
    print_pause(
        "The porple of the village hear what you've done for them and greet you\n"
        "You've become the village's savior!",
        2,
    )
    play_again()


def cave():
    print_pause(
        "the player is now stranded in a cave, nothing but darkness inside\n"
        "you hear noise, it is a lion\n",
        3,
    )
    print_pause("What will you do?\n", 3)
    while True:
        cave_response = input(
            "Fight the lion or escape\n"
            "Press 1 to fight the lion\n"
            "Press 2 to escape\n",
            3,
        )
        if "1" in cave_response:
            fight()
        elif "2" in cave_response:
            print_pause(
                "You have escaped and abandoned the people!\n"
                "!!!!!!!!!!GAME OVER!!!!!!!!!!",
                2,
            )
        else:
            print_pause("Wrong Selection Mate!!!!!!", 2)
        play_again()


def house():
    print_pause("You open the door of the house --> Enter\n", 2)
    print_pause("an old Witch finds you\n", 2)
    print_pause("You dare enter my houuse she says\n", 2)
    print_pause("Casts a spell on you\n", 2)
    print_pause(
        "!!!!!!!!!! GAME OVER !!!!!!!!!! \n" "DO NOT PLAY WITH WITCHES BOY\n", 2
    )
    play_again()


def act_I():
    while True:
        choice = input(
            """Enter 1 to knock on the door of the house
                       Enter 2 to peer into the cave
                       What would you like to do?
                       Please enter 1 or 2 -->: """
        )
        if choice == "1":
            print_pause("You Enter the house and see the unexpected !!!!!!!", 2)
            house()
        elif choice == "2":
            print_pause(
                "Who dares enter the cave that has been sealed for 100 years?", 2
            )
            cave()
        else:
            print_pause("Wrong Selection mate, read the lines !!!!!!!!!", 2)


def play_again():
    while True:
        repeat = input("Do you wish to go on another adventure? (y/n) --> ").lower()
        if repeat == "y":
            time.sleep(4)
            main()
        elif repeat == "n":
            print_pause("Your adventure ends here, good luck in future endvours !", 2)
        else:
            print_pause("Wrong input mate!!!!!!!!!!!!!!!!!!!!!!!!!!!", 2)


if __name__ == "__main__":
    main()
