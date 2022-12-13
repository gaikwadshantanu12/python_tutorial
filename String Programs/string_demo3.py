# WAP to print all characters with index numbers

string = input("Enter any string - ")

print("\n\nIn Forward Direction - ")
i = 0
while i < len(string):
    print(f"Index No {i} - {string[i]}")
    i = i + 1

print("\n\nIn Backward Direction")
i = len(string) - 1
while i >= 0:
    print(f"Index No {i} - {string[i]}")
    i = i - 1

