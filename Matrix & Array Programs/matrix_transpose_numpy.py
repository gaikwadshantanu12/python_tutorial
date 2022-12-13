import numpy as np

r,c = [int(x) for x in input("\nEnter dimensions - ").split()]
m1 = [[int(x) for x in input("Row - %d : "%(i+1)).split()] for i in range(r)]
m1 = np.array(m1)
m2 = m1.transpose()         # we can also use m2 = m1.T

print("Transpose - ",m2)