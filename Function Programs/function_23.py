# WAP for fibonacci series using function
# 1. Without recursion
# 2. With recursion

# Method 1
"""
def fib(n):
    print("0\t1",end="\t")    # for 2 terms
    x = 0
    y = 1
    for i in range(n-2):            # for 8 terms
        sum = x+y
        print(sum,end="\t")
        x = y
        y = sum

x = int(input("Enter how many terms ? : "))
fib(x)
"""

# Method 2
def fib(n):
    if n <= 1:
        return n

    return (fib(n-2) + fib(n-1))

x = int(input("Enter how many terms ? : "))
for i in range(x):
    print(fib(i),end="\t")