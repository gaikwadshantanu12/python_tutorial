# WAP to count occurrences of given character in given string

"""
# Method 1
s = input("Enter your string - ")
ch = input("Enter character to search - ")
count = 0
for i in s:
    if ch == i:
        count = count + 1

print(f"'{ch}' occurs {count} time(s) in '{s}'")
"""

# Method 2
s = input("Enter your string - ")
ch = input("Enter character to search - ")
print(f"'{ch}' occurs {s.count(ch)} time(s) in '{s}'")