while( True ):
    num1 = int(input("\nEnter first number - "))
    num2 = int(input("Enter second number - "))
    print("\n0. Exit\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Floor Division\n6. Modulus\n7. Power")
    ch = input(f"\nSelect the operation you want to perform on {num1} and {num2} - ")

    if ch == "0":
        break
    elif ch == "1":
        print(f"Addition of {num1} and {num2} is {num1 + num2}")
    elif ch == "2":
        print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
    elif ch == "3":
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
    elif ch == "4":
        print(f"Division of {num1} and {num2} is {num1 / num2}")
    elif ch == "5":
        print(f"Floor Division of {num1} and {num2} is {num1 // num2}")
    elif ch == "6":
        print(f"Modulus of {num1} and {num2} is {num1 % num2}")
    elif ch == "7":
        print(f"{num1} raised to {num2} is {num1 ** num2}")
    else:
        print("Invalid choice...Enter correct choice")
