# WAP to iterate over two lists of same length simultaneously

a = eval(input("Enter list 1 of numbers [] - "))
b = eval(input("Enter list 2 of numbers [] - "))

for (x,y) in zip(a,b):
    print(x,y)