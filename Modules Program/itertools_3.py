"""
WAP to read and print all possible spelling of same length that can be formed from letters of given word. (Letters can repeat)
"""

import itertools as itr
w = input("Enter any word : ")
for x in itr.product(w,repeat=len(w)):
    print("".join(x))