# WAP to find the list in a list of list whose sum of element is the highest

print("\nEnter Nested List :")
a = [[int(x)for x in input("Sublist %d - "%(i+1)).split()] for i in range(4)]
j = 1
max = sum(a[0])
while j < len(a):
    if sum(a[j]) > max:
        max = sum(a[j])
        pos = j

    j+=1

print("Sublist with highest sum - ",a[pos])