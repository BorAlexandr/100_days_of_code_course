#I Create simple program in this course that calcuate tips.

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round((total_bill + ((total_bill * tip) / 100)), 2) / people}")
