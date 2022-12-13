import numpy as np

# Method 3
row , column = [int(x) for x in input("Enter Rows X Columns - ").split()]
m = np.ones((row,column),dtype=int)         # if we did not give dtype parameter it will print in float

print(m)