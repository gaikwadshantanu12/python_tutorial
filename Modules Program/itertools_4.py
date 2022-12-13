# Add elements of list of unequal length

import itertools as itr
l1 = [1,2,3]
l2 = [4,5,6,7]
c = []
for x,y in itr.zip_longest(l1,l2,fillvalue=0):
    c.append(x+y)
print(c)