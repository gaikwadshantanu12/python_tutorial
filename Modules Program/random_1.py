# Generate five 6-digit random numbers
import random as r
for i in range(5):
    print(r.randint(100000,999999))
    # or
    # print(r.randint(0,9),r.randint(0,9),r.randint(0,9),r.randint(0,9),r.randint(0,9),sep="")
    # beginning and end is included

# No repetition in random modules