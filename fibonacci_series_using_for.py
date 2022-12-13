# WAP to print fibonacci series using for loop

terms = int(input("Enter no. term for fibonacci series - "))
print("Fibonacci Series - ")
x = 0
y = 1
print("0\t1",end="\t")
terms = terms - 2

for i in range(terms):
    sum = x + y
    print(sum,end="\t")
    x = y
    y = sum