# WAP to sort characters of string first alphabets and then digits

"""
Example :
Input - B4A2D3
Output - ABD234
"""

s = input("Enter alpha-numeric string - ")
result1 = ""
result2 = ""
new_col = sorted(s)

for i in new_col:
    if i.isalpha():
        result1 = result1 + i
    if i.isdigit():
        result2 = result2 + i

print(result1+result2)