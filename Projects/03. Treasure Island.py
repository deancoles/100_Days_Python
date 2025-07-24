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
print("The goal of all travellers on this island is to find the treasure.")
name = input("\nWhat is the name of the great traveller?:\n").capitalize()

# Monster name
if name == "Morgan":
    monster = "Pickle Morgan"
else:
    monster = "a Wild Morgan"

# Choices
crossroad = input(f"{name} is at a cross road, they can either go left or right, what way will {name} go?\n").lower()
if crossroad == "left":
    swim = input(f"{name} arrived at a lake. There is a small island in the middle of the lake. "
                 f"What will {name} decide? wait for a boat or swim across?\n").lower()

    if swim == "wait":
        door = input(f"After waiting a boat arrived and took {name} to the island. "
                     f"On the island there are three doors side by side, one is Red, one is Yellow,"
                     f" and the other is blue. What door should {name} choose to open?\n").lower()

        if door == "yellow":
            print(f"\n{name} opened the door and a treasure chest magically appeared from out of nowhere! "
                  f"{name} lived like royalty until the end of time.")
        else:
            print(f"{name} died after being attacked by {monster}.")

    else:
        print(f"{name} died after being attacked by {monster}.")

else:
    print(f"{name} died after being attacked by {monster}.")
