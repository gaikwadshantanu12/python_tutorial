"""WAP to read age from user and print child if age is below 18. Adult if age is 18 or above. Senior citizen if age is 65 or higher"""

age = int(input("Enter your age - "))
if age < 18:
    print("You are child")
elif age < 65:
    print("You are adult")
elif age < 100:
    print("You are senior citizen")
else:
    print("Incorrect age")