"""
WAP to read list of 5 colors and print all possible combinations taken given number of colors at a time

1. Order Matters (permutations)
2. Order does not matters (combinations)
"""

"""
# Solution for 1.

import itertools as itr
colors = ['RED','GREEN','BLUE']
r = int(input("Enter number of colors to be taken : "))
for x in itr.permutations(colors,r):
    print(x)
"""

# Solution For 2
import itertools as itr
colors = ['RED','GREEN','BLUE','WHITE','BLACK']
r = int(input("Enter number of colors to be taken : "))
for x in itr.combinations(colors,r):
    print(x)