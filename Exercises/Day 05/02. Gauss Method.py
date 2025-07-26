# This program adds all the numbers from 1 to 100 (inclusive)
# It's based on Gauss's method to quickly calculate the total sum

# Start with a total of 0
total = 0

# Loop through every number from 1 to 100
for number in range(1, 101):
    # Add the current number to the total
    total += number

# Print total
print(total)