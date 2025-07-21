#Dean Solution
print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Convert the tip percentage into a decimal (e.g., 10 becomes 0.10)
tip_cost = tip / 100

# Calculate tip amount (bill * tip_cost), add it to the original bill. Round to 2 decimal places.
total = round(bill + (bill * tip_cost), 2)

# Divide the total by the number of people to get each person's share
cost = total / people

# Round the individual share to 2 decimal places
final_amount = round(cost, 2)

# Print overall total and each person's share of the bill
print (f"\nOverall total: £{total}")
print(f"Each person should pay: £{final_amount}")


# # Angela Solution
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? £"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill +total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: £{final_amount}")
