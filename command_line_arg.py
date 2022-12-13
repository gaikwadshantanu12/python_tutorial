# WAP to perform addition of integers supplied from command line

import sys
"""
a = int(sys.argv[1])
b = int(sys.argv[2])
print("\nAddtion =",a+b)
"""
a = [int(x) for x in sys.argv[1:]]
print(f"Addition : {sum(a)}")