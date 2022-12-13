# WAP to print the numbers of a specified list after removing even numbers from it
# Note - Try to use comprehension

a = eval(input("Enter list of numbers [] - "))
"""
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)

print(b)
"""
#or

a = [i for i in a if i % 2 != 0]
print(a)