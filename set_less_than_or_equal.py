# WAP to read two strings and check if all characters of string 1 appears in string 2 at least once

# Note - s1 <= s2 or s1.issubset(s2)

s1 = input("Enter string 1 - ")
s2 = input("Enter string 2 - ")
if set(s1) <= set(s2):
    print("All characters of string 1 appears in string 2")
else:
    print("All characters of string 1 does not appears in string 2")