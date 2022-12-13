# WAP to sort a list according to the length of the elements

l1 = eval(input("Enter String List In [] - "))

print(f"\n\nOriginal List - \n{l1}")

l1.sort(key=len)

print(f"\n\nSorted List - \n{l1}")