# WAP to find number of occurrences of each letter in a string by using dictionary

s = input("Enter any string - ")
d = {}
for x in s:
    d[x] = d.get(x,0) + 1

for k,v in d.items():
    print(f"{k} occurs {v} items")

"""
Method 2 - collection modules

import collections as clt
s = input("Enter any string - ")
d = dict(clt.Counter(s))
print(d)
"""