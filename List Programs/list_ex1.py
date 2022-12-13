# WAP to remove duplicates from a list

l1 = eval(input("Enter list elements in [] - "))
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)

print(f"Original List - {l1}")
print(f"After Removing Duplicates - {l2}")