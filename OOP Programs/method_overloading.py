# Method / Function Overloading

# Method 1
def add(a=None, b=None, c=None):        # default arguments and in python "None = False"
    if a and b and c:
        return a+b+c
    elif a and b:
        return a+b
    elif a:
        return a
    else:
        return 0

"""
# Method 2
def add(*args):     # variable lenght arguments
    return sum(args) 
"""

print("0 Parameter :",add())
print("1 Parameter :",add(10))
print("2 Parameter :",add(10,20))
print("3 Parameter :",add(10,20,30))