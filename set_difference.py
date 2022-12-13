# WAP to read two string and print characters that are in A but no in B
# Note - A - B

s1 = input("Enter string 1 - ")
s2 = input("Enter string 2 - ")
print("\nCharacter in A but not in B - \n",set(s1) - set(s2))