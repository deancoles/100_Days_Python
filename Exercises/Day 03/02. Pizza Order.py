# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

"""
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill +=2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill +=3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
