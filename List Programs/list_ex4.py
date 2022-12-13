# WAP to check a list is empty or not

l = eval(input("Enter list elements in [] - "))
if len(l) == 0:
    print("List is empty")
else:
    print("List is not empty")

# Logically empty list is false
"""
if not a:
    print("List is empty")
else:
    print("List is not empty")
"""
