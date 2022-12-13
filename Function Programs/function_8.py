# WAP define a function which prints addition of given integers. Function should take any number of paramters

def additon(*args):
    return sum(args)

# args is a tuple
print("Additon =",additon(10,20,30,40,50,60))

"""
we can also do :

a,b,c,d = 10,20,30,40
print("Addition =",addition(a,b,c,d))
"""

"""
if we do :
l = [10,20,30,40,50]
print("Addition =",addition(l))

It will give error because we can't pass list to sum function as it is a single parameter for sum function
To avoid this we can do this :
print("Addition =",addition(*l))
"""