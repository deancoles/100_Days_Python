print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
name = input("What is the name of the great traveller?: ")

# Monster name
if name == "morgan" or name == "Morgan" or name == "MORGAN":
    monster = "Pickle Morgan"
else:
    monster = "Wild Morgan"

# Choices
crossroad = input(f"{name} is at a cross road, they can either go left or right, what way did {name} go? ")
if crossroad == "left" or crossroad == "Left" or crossroad == "LEFT":
    swim = input(f"{name} arrived at a lake. There is a small island in the middle of the lake. "
                 f"What did {name} decide? did they wait for a boat or swim across? ")

    if swim == "wait" or swim == "Wait" or swim == "WAIT":
        door = input(f"After waiting a boat arrived and took {name} to the island ")

        if door == "yellow" or door == "Yellow" or door == "YELLOW":
            print(f"{name} found the treasure and lived like royalty until the end of their days.")
        else:
            print(f"{name} died after being attacked by a {monster}.")

    else:
        print(f"{name} died after being attacked by a {monster}.")

else:
    print(f"{name} died after being attacked by a {monster}.")
