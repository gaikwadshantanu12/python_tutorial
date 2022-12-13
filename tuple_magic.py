# WAP to remove an empty tuple(s) from a list of tuples

# Sample data : [(),(),(",),('a','b'),('a','b','c'),('d',)]

a = [(),(),('',),('a','b'),('a','b','c'),('d',)]
b = []
for x in a:
    if len(x)!=0:
        b.append(x)
"""
In one statement -
b = [x for x in a if x]

Note -
x = True for non empty
x = false for empty
"""
print(b)