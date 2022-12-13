# WAP to calculate factorial through function
# 1. without recursion
# 2. with recursion
# Do not use ready made function or module

# Method 1 - Without recursion
"""
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i

    return f

x = int(input("Enter number : "))
y = factorial(x)
print(f"{x} != {y}")        #factorial symbol
"""

# Method 2 - With Recursion
def factorial(n):
    if n == 1:
        return 1

    f = n*factorial(n-1)
    return f

x = int(input("Enter number : "))
y = factorial(x)
print(f"{x} factorial = {y}")
