# WAP to calculate power through function
# 1. Without recursion
# 2. Through recursion
# Do not use ready made functions or modules

# Method 1
"""
def power(x,y):
    p = 1
    for i in range(y):
        p = p * x
    return p


base = int(input("Enter base number : "))
index = int(input("Enter index number : "))
print("Power = ",power(base,index))
"""

# Method 2
def power(x,y):
    p = 1
    if y == 1:
        return x

    p = x * power(x,y-1)
    return p

base = int(input("Enter base number : "))
index = int(input("Enter index number : "))
print("Power = ",power(base,index))