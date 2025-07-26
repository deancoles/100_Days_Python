# Original
import random

# Start scores for player and CPU
play_total = 0
cpu_total = 0

# Choose number of rounds
target_wins = int(input("Play best of how many rounds? (3 or 5): "))
rounds_to_win = (target_wins // 2) + 1

# Function to run ONE round of the game
def game(play_total, cpu_total):

    # ASCII art for each move
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

    game_images = [rock, paper, scissors]

    # Ask user to choose Rock, Paper or Scissors
    try:
        choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    except ValueError:
        print("Invalid input (not a number). You lose this round.")
        cpu_total += 1
        return play_total, cpu_total

    # Check if the choice is valid BEFORE using it
    if choice < 0 or choice >= 3:
        print("Invalid choice entered. You lose this round.")
        cpu_total += 1
        return play_total, cpu_total

    # Only runs if the choice is valid
    print("\nYou chose:")
    print(game_images[choice])

    # Randomly choose for CPU
    cpu_choice = random.randint(0, 2)
    print("\nCPU choose: ")
    print(game_images[cpu_choice])

    # Decide winner and update the scores
    if choice == 0 and cpu_choice == 2:
        print("You win")
        play_total += 1
    elif choice == 2 and cpu_choice == 0:
        print("You lose")
        cpu_total += 1
    elif choice > cpu_choice:
        print("You win")
        play_total += 1
    elif choice < cpu_choice:
        print("You lose")
        cpu_total += 1
    elif choice == cpu_choice:
        print("You have drawn")

    # Show the updated scores
    print(f"\nCurrent Score → You: {play_total} | CPU: {cpu_total}\n")

    # Return the updated scores to the main loop
    return play_total, cpu_total

# Main Loop – keep playing rounds until someone wins 2
while play_total < rounds_to_win and cpu_total < rounds_to_win:
    play_total, cpu_total = game(play_total, cpu_total)
# Announce overall winner
if play_total == rounds_to_win:
    print(f"🎉 You won the best of {target_wins} match!")
else:
    print(f"💻 CPU won the best of {target_wins} match. Better luck next time!")

