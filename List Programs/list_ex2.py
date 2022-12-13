# WAP that takes two list and checks if they have at least one common member

l1 = eval(input("Enter list1 elements in [] - "))
l2 = eval(input("Enter list2 elements in [] - "))

for x in l1:
    if x in l2:
        print(f"{x} is first common element")
        break

# Else of for loop
else:
    print("No common element found in two lists")