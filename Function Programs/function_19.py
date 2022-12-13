# WAP menu - driven program using function

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def power(a,b):
    return a ** b

switch = {1:add,2:sub,3:mul,4:div,5:power}

while(True):
    print("\n\n***** MENU *****\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n0. Exit/Stop")
    choice = int(input("Enter Your Choice : "))
    if choice in range(1,6):
        x,y = [eval(i) for i in input("Enter two numbers separated by space : ").split()]

    if choice == 0:
        break
    elif choice not in range(1,6):
        print("\nInvalid Choice")
    else:
        print("Result is : ",switch.get(choice)(x,y))

print("Thank You !")