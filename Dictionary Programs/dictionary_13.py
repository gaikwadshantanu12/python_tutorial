# WAP to combine two dictionary adding values for common keys

d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}
d3 = d1.copy()

for k,v in d2.items():
    if k in d3:
        d3[k] = d3[k] + v       # add and update operation
    else:
        d3[k] = v               # add operation

print("Result -\n",d3)


"""
Using Module

import collections as clt
d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}
d3 = dict{clt.Counter(d1)+clt.Counter(d2)}
print("Result -",d3)

If we donot use dict{} then it will be counter object
"""

"""
Counter object for string
s = "hello world"
print(clt.Counter(s))

Output - Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
"""