# WAP to check whether a specified list is sorted or not.

l1 = eval(input("Enter List In [] - "))
copy_l1 = l1.copy()
copy_l1.sort()

if l1 == copy_l1:
    print("Your list is in sorted order")
else:
    print("Your list isn\'t in sorted order")

