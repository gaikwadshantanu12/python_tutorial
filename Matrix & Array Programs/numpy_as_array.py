# WAP to take input 10 numbers and multiply it by given number

import numpy as np

a = [int(x) for x in input("Enter 10 integers - ").split()]
n = int(input("Enter the number to multiply - "))
a = np.array(a)
a = a * n
print(a)

"""
or

for x in a:
    print(x,end=" ")
"""