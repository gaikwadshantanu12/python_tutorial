# Generate random password of length-6 where 1,3,5 are alphabet and 2,4,6 are digits

import random as r
ls = []
"""
for i in [1,3,5]:
    ch = r.randint(ord('A'),ord('Z')+1)
    ls.insert(i-1,chr(ch))

for j in [2,4,6]:
    ch = r.randint(0,9)
    ls.insert(j-1,str(ch))
"""
for i in range(1,7):
    if i%2 == 0:
        ch = r.randint(0, 9)
        ls.insert(i - 1, str(ch))
    else:
        ch = r.randint(ord('A'), ord('Z') + 1)
        ls.insert(i - 1, chr(ch))

print("".join(ls))
