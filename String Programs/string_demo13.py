# WAP to read mobile number and check if it can be a valid number

mob = input("Enter mobile number - ")

if len(mob) == 10 and mob.isdigit():
    print("Valid mobile number")
else:
    print("Invalid mobile number")