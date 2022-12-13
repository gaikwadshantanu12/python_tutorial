# WAP to check if two string are anagrams or not

"""
Anagrams - If two strings contains exactly same letters same number of times then two string are anagrams

Example -
string 1 = silent
string 2 = listen

Algorithms :
Step 1 - Input 2 strings
Step 2 - sorted list of string 1
Step 3 - sorted list of string 2
"""

s1 = input("Enter String 1 - ")
s2 = input("Enter String 2 - ")
lst_1 = sorted(s1)
lst_2 = sorted(s2)

if lst_1 == lst_2:
    print(f"'{s1}' and '{s2}' are Anagrams")
else:
    print(f"'{s1}' and '{s2}' aren\'t Anagrams")