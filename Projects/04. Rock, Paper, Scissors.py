# Original
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Name Entry
user = input("Enter your name: ")
rival = input("Enter your rival's name: ")

# User Choice
choice = int(input(f"What do you choose {user}? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# User GUI
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid code")

# CPU Choice and Determination
cpu_choices = [0, 1, 2]
cpu_choice = random.choice(cpu_choices)

# CPU GUI
if cpu_choice == 0:
    print(rock)
elif cpu_choice == 1:
    print(paper)
elif cpu_choice == 2:
    print(scissors)
else:
    print("Invalid code")

# Calculations
if choice == cpu_choice:
    print("You have drawn")
elif choice == 1 and cpu_choice == 0:
    print(f"{user}'s Paper beats {rival}'s Rock")
elif choice == 0 and cpu_choice == 1:
    print(f"{rival}'s Paper beats {user}'s Rock")
elif choice == 2 and cpu_choice == 0:
    print(f"{user}'s beats the {rival}'s Scissors")
elif choice == 0 and cpu_choice == 2:
    print(f"{rival}'s Rock beats {user}'s Scissors")
elif choice == 2 and cpu_choice == 1:
    print(f"{user}'s Scissors beats the {rival}'s Paper")
elif choice == 1 and cpu_choice == 2:
    print(f"{rival}'s Scissors beats {user}'s Paper")
