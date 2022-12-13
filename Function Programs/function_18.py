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

while(True):
    print("\n\n***** MENU *****\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n0. Exit/Stop")
    choice = int(input("Enter Your Choice : "))
    if choice in range(1,6):
        x,y = [eval(i) for i in input("Enter two numbers separated by space : ").split()]

    if choice == 0:
        break
        # exit()
    elif choice == 1:
        print("Addition : ",add(x,y))
    elif choice == 2:
        print("Subtraction : ",sub(x,y))
    elif choice == 3:
        print("Multiplication : ",mul(x,y))
    elif choice == 4:
        print("Division : ",div(x,y))
    elif choice == 5:
        print("Power : ",power(x,y))
    else:
        print("Invalid Choice")


print("Thank You !")