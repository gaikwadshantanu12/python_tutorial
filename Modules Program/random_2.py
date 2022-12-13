# generate five anagrams of given word

import random as r
s = "shantanu"
ls = list(s)
for i in range(5):
    r.shuffle(ls)
    # shuffle is in place replacing
    print("".join(ls))

"""
Logic : 

S1 -> Convert String To List
S2 -> Shuffle The List
S3 -> Join The List To String
"""