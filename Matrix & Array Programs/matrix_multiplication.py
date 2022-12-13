print("\nEnter Matrix 1 :")
m1 = [[int(x)for x in input("Row %d - "%(i+1)).split()] for i in range(3)]

print("\nEnter Matrix 2 :")
m2 = [[int(x)for x in input("Row %d - "%(i+1)).split()] for i in range(3)]

m3 = [[0 for j in range(3)] for i in range(3)]          # All values are 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            m3[i][j] = m3[i][j] + m1[i][k] * m2[k][j]


"""
# level of comprehension of above 3 loops

m3 = [[sum(a*b for a,b in zip(r,c)) for c in zip(*m2)] for r in m1]
"""
print("\nMultiplication : \n",m3)