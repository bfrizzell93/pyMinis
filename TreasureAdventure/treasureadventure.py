print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


crossroads_answer = input("You come to a crossroads. Where would you like to go? Type \"left\" or \"right\" \n")
if crossroads_answer == "left":
    river_answer = input("You come to a river. What do you do? Swim across or wait? \n")
    if river_answer == "swim":
        print("The current is too strong! You can't fight it. You drown. Game over.")
    if river_answer == "wait":
        door_answer = input("You wait until nightfall. A group of adventurers comes along and takes you to a strange room with 3 doors. Which door do you pick? red, blue or yellow? \n")
        if door_answer == "red":
            print("You open the door and you are pulled through a portal into the fire plane. Game over.")
        if door_answer == "yellow":
            print("You open the door to a mountain of gold and riches. You win!")
        if door_answer == "blue":
            print("You walk into the torture room. GAME OVER.")

if crossroads_answer == "right":
    print("You are attacked by bandits. Game over.")