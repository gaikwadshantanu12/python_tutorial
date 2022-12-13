# WAP to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30

a = []

"""
for x in range(1,31):
    a.append(x*x)

print(a[5:])
"""

a = [x*x for x in range(1,31)]
print(a[5:])