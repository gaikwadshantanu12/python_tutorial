# WAP to convert string into dictionary

s = 'Swapnil=23,Ganesh=20,Krishna=4,Dhariya=1'
l = s.split(",")
# print(l)
b = []

for x in l:
    y = x.split("=")
    b.append(y)
d = dict(b) # output in ready but we have to convert value into integer datatype

for k,v in d.items():
    d[k] = int(v)

print(d)


"""
Method 2 short method -

s = 'Swapnil=23,Ganesh=20,Krishna=4,Dhariya=1'
l = s.split(",")
b = {}

for x in l:
    y = x.split("=")
    b.update({y[0]:int(y[1])})

print(b)
"""