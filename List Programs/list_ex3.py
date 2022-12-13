# WAP to create list of common elements

l1 = eval(input("Enter list1 elements in [] - "))
l2 = eval(input("Enter list2 elements in [] - "))
l3 = []

for item in l1:
    if item in l2:
        if item not in l3:
            l3.append(item)

print(f"\n\nList 1 - {l1}")
print(f"List 2 - {l2}")
print(f"List of Common Elements - {l3}")