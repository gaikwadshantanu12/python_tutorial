# WAP to sort(ascending and descending) a dictionary by value

import operator as op
d = {1:5,3:7,5:10,2:20,9:12,7:15}

print("Sorting According To Value :")
print("Ascending Value -",sorted(d.values()))
print("Descending Value -",sorted(d.values(),reverse=1))

print("\nSorting According To Key :")
print("Ascending Key -",sorted(d))
print("Descending Key -",sorted(d,reverse=1))

print("\nSorting List Of Pair (1): (Only Used d.items())")
print("Ascending Pair -",sorted(d.items()))
print("Descending Pair -",sorted(d.items(),reverse=1))
# If we use d.items() it will compare with respect to key

print("\nSorting List Of Pair (2): (Used d.items() with operator module)")
print("Ascending Pair -",sorted(d.items(),key=op.itemgetter(1)))
print("Descending Pair -",sorted(d.items(),reverse=1,key=op.itemgetter(1)))
# Now it sorts according to value

"""
Note we can also use lambda function for above operation

sorted(d.items(),key=lambda t:t[1])
"""