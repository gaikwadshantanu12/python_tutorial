# WAP to find second highest value in given list of numbers

"""
l1 = eval(input("Enter List In [] - "))
l2 = l1[:]
item = max(l2)
l2.remove(item)
maximum = max(l2)
print(f"Second Highest Value in Above List - {maximum}")
"""

l1 = eval(input("Enter List In [] - "))
print(f"\n\nEntered List - \n{l1}")
s = set(l1)
l1 = list(s)
l2 = l1[:]
item = max(l2)
l2.remove(item)
maximum = max(l2)
print(f"\n\nSecond Highest Value in Above List - {maximum}")