"""
WAP to add all elements of nested list through only sum function

for ex : if a = [[1,2,3],[4,5,6]], Result is 21

It is single statement task. No loop, no comprehension. Only call to BIF function
"""

a = [[1,2,3],[4,5,6]]
print(sum(sum(a,[])))
