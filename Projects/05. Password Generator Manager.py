import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Variable to hold password
password = ""

# Loop through characters in the range between 0 and input
for char in range(0, nr_letters):
    # Add character to password
    password += random.choice(letters)

# Loop through characters in the range between 0 and input
for char in range(0, nr_symbols):
    # Add symbol to password
    password += random.choice(symbols)

# Loop through characters in the range between 0 and input
for char in range(0, nr_symbols):
    # Add number to password
    password += random.choice(numbers)

# Create variable for password in list format
password_as_list = list(password)
# Shuffle password
random.shuffle(password_as_list)
# Return shuffled password to variable
password = "".join(password_as_list)

# Return password to the user
print(f"Your password is {password}")