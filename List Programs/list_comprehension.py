# WAP to create list of all integers from 100 to 200 that are divisible by n

"""
Method No 1

n = int(input("Enter the number - "))
a = []
for x in range(100,201):
    if x % n == 0:
        a.append(x)

print(f"Number divisible by {n} are {a}")
"""

# Method No 2
n = int(input("Enter the number - "))
a = [x for x in range(100,201) if x%n==0]
print(a)