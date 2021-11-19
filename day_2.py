#I Create a program using maths evaluates and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
left_ages = 90 - int(age)
#Write your code below this line 👇
print(f"You have {left_ages * 365} days, {left_ages * 52} weeks, and {left_ages * 12} months left.")
