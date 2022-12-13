# WAP for follwoing requirement

"""
Input - a4b3c2
Output - aaaabbbcc
"""

s = input("Enter string in format (a4b3c2) - ")
res = ""

for x in s:
    if x.isdigit():
        res = res + res[-1] * (int(x)-1)
    else:
        res += x

print(res)