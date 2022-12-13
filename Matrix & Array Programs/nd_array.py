# WAP to generate 3*4*6 3D array whose each element is *

a = []

for i in range(3):
    sub = []
    for j in range(4):
        s = []
        for k in range(6):
            s.append("*")
        sub.append(s)
    a.append(sub)

print(a)

"""
Comprehension of above :

a = [[["*" for k in range(6)] for j in range(4)] for i in range(3)]
"""