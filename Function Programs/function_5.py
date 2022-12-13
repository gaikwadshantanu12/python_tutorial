# WAP to print even from a given list using function

def printEven(a):
    print("Even Numbers :")
    for x in a:
        if x % 2 == 0:
            print(x,end=" ")

l = eval(input("Enter list in [] - "))
# ls = [x*x for x in range(10)]
printEven(l)
