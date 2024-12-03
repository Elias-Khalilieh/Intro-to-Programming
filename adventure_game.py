import time
import random

enemies = ["Troll","Dragon","Witch","Ghoul","Alien"]
weapons = ["Sword","Dagger","Crossbow","Pistol","Flamethrower"]


enemy = random.choice(enemies)
weapon = random.choice(weapons)
##################################################################################################################################################################################

def main():
    intro(enemy,weapon)
    act_I()

def intro(enemy,weapon):
    
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere arounf here and has been terrifying the nearby village")
    print_pause("In front of you is a house")
    print_pause("to your right is a dark cave")
    print_pause(f"in your hand you hold a rusty not so much effective {weapon}")

def print_pause(message):
    print(message)
    time.sleep(2)

def fight():
    print_pause(f"you hold your weapon and swing it with great might to the {enemy} 's head")
    print_pause("The porple of the village hear what you've done for them and greet you\n"
                "You've become the village's savior!")
    
def cave():
    print_pause("the player is now stranded in a cave, nothing but darkness inside\n"
                "you hear noise, it is a lion\n")
    print_pause("What will you do?\n")
    cave_response = input("Fight the lion or escape\n"
                          "Press 1 to fight the lion\n"
                          "Press 2 to escape\n")
    if "1" in cave_response:
        fight()
    if "2" in cave_response:
        print_pause("You have escaped and abandoned the people!\n"
                    "!!!!!!!!!!GAME OVER!!!!!!!!!!")
        
    
    
def house():
    print_pause("You open the door of the house --> Enter\n")
    print_pause("an old Witch finds you\n")
    print_pause("You dare enter my houuse she says\n")
    print_pause("Casts a spell on you\n")
    print_pause("!!!!!!!!!! GAME OVER !!!!!!!!!! \n"
                "DO NOT PLAY WITH WITCHES BOY\n")


def act_I():
    choice = input ("""Enter 1 to knock on the door of the house
                       Enter 2 to peer into the cave
                       What would you like to do?
                       Please enter 1 or 2 -->: """)
    if choice == "1":
        print_pause("You Enter the house and see the unexpected !!!!!!!")
        house()
    if choice == "2":
        print_pause("Who dares enter the cave that has been sealed for 100 years?")
        cave()
    else: 
        print("Wrong Selection mate, read the lines !!!!!!!!!")
        act_I()


main()