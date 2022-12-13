# WAP to print a specified list after removing the 0th, 5th and 5th elements

a = eval(input("Enter list in [] - "))
b = [y for (x,y) in enumerate(a) if x not in [0,4,5]]
print(b)