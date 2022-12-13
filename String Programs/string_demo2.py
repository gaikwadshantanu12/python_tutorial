# WAP to print string in forward and backward direction using while loop

string = input("Enter any string - ")

print("\n\nIn Forward Direction - ")
i = 0
while i < len(string):
    print(string[i],end="")
    i = i + 1

print("\n\nIn Backward Direction")
i = len(string) - 1
while i >= 0:
    print(string[i],end="")
    i = i - 1