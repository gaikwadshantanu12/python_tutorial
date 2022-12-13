import numpy as np

r,c = [int(x) for x in input("\nEnter dimensions - ").split()]

print("\n\nMatrix No 1")
m1 = [[int(x) for x in input("Row - %d : "%(i+1)).split()] for i in range(r)]
m1 = np.array(m1)

print("\n\nMatrix No 2")
m2 = [[int(x) for x in input("Row - %d : "%(i+1)).split()] for i in range(r)]
m2 = np.array(m2)

m3 = m1 + m2
print("Addition - ",m3)

"""
Note - Same for Subtraction
"""