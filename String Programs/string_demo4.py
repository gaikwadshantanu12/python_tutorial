# WAP to print string in forward and backward direction using for loop

s = input("Enter any string - ")
print("Forward - ",end=" ")
for ch in s:
    print(ch,end="")

print("\nBackward - ",end=" ")
for ch in s[::-1]:
    print(ch,end="")