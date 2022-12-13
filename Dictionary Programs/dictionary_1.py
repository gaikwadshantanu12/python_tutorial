# WAP to read key and value from user and create dictionary

d = {}
n = int(input("Enter length - "))
for i in range(n):
    key = eval(input("\nEnter keys - "))
    value = eval(input("Enter value - "))
    d[key] = value

print("Dictionary - \n",d)

"""
Method 2 - 

d = eval(input("Enter dictionary in key:value format - "))
print("Dictionary - ")
"""