# WAP to convert more than one list to nested dictionary

"""
Original Strings :
['S001','S002','S003','S004']
['Raymond','Peter','Blackberry','Polo']
[85,98,89,92]

Nested Dictionary :
{'S001':{'Raymond':85},'S002':{'Peter':98},'S003':{'Blackberry':89},'S004':{'Polo':92}}
"""

a = ['S001','S002','S003','S004']
b = ['Raymond','Peter','Blackberry','Polo']
c = [85,98,89,92]

d = {}
for x,y,z in zip(a,b,c):
    d[x] = {y:z}

print(d)

"""
d = {x:{y:z} for x,y,z in zip(a,b,c)}
"""