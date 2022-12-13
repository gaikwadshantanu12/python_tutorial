# WAP for following output

"""
INPUT - A2B3C4
OUTPUT - ACBECG
"""

s = input("Enter the string - ")
res = ""
for x in s:
    if x.isdigit():
        res = res + chr(ord(res[-1]) + int(x))
    else:
        res = res + x

print(res)