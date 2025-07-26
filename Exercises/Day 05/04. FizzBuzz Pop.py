def check_conditions(i):
    # Start with an empty string to build the result
    result = ""
    # If the number contains the digit 3, add "Pop"
    if '3' in str(i):
        result += "Pop"
    # If the number is divisible by 3, add "Fizz"
    if i % 3 == 0:
        result += "Fizz"
    # If the number is divisible by 5, add "Buzz"
    if i % 5 == 0:
        result += "Buzz"
    # Return result if any condition matched, otherwise return the number itself
    return result if result else str(i)

# Define a function to run FizzBuzz
def fizz_buzz_twist(n):
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        print(check_conditions(i))

# Call the function for numbers 1 to 100
fizz_buzz_twist(100)