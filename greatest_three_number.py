# Find greatest among three numbers

num1 = eval(input("Enter First Number - "))
num2 = eval(input("Enter Second Number - "))
num3 = eval(input("Enter Third Number - "))

if num1 > num2:
    if num1 > num3:
        print("First number is greatest ie.", num1)
    else:
        print("Third number is greatest ie.", num3)
else:
    if num2 > num3:
        print("Second number is greatest ie.", num2)
    else:
        print("Third number is greatest ie.", num3)