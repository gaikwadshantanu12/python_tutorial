# WAP to read two strings and check if both contains same characters (order does not matter)

s1 = input("Enter string 1 - ")
s2 = input("Enter string 2 - ")
if set(s1) == set(s2):
    print("string 1 and string 2 contains same characters")
else:
    print("string 1 and string 2 do not contains same characters")