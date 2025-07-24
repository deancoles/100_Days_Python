# Optimised
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

# Game Images
game_image = [rock, paper, scissors]

# User Choice
user_choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

# CPU Choice and Determination
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_image[computer_choice])

# Invalid Entry
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
# Scissors over Rock
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
# Scissors over Paper & Paper over Rock
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
# Both choose same item
elif computer_choice == user_choice:
    print("It's a draw!")