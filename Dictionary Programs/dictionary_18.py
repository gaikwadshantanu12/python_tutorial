# WAP to find highest three values and corresponding keys in a dictionary

"""
data = {'a':70, 'b':30, 'c':90, 'd':120, 'e':5}
"""

data = {'a':70, 'b':30, 'c':90, 'd':120, 'e':5}
b = sorted(data.items(), key=lambda  t:t[1])

print(b[-1])
print(b[-2])
print(b[-3])

"""
Method 2

import heapq as hq
data = {'a':70, 'b':30, 'c':90, 'd':120, 'e':5}
b = hq.nlargest(3,data,key=data.get)
for x in b:
    print(x,":",data[x])
"""