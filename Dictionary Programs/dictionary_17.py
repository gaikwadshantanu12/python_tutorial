# WAP to combine values in python list of dictionaries

"""
Sample Data : [{'item':'item1','amount':400}, {'item':'item2','amount':300},{'item':'item1','amount':750}]

expected output - {'item1':1150,'item2':300}
"""

import collections as clt

data = [{'item':'item1','amount':400},
        {'item':'item2','amount':300},
        {'item':'item1','amount':750}]

d = clt.Counter()
for x in data:
    d[x['item']] = d[x['item']] + x['amount']

print(d)
