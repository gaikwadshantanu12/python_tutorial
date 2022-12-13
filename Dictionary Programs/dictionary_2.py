# WAP to generate and print a dictionary that contains a number (between 1 and n) in the form (x,x*x)

n = int(input("Enter nth value - "))
d = {}
for item in range(1,n+1):
    d[item] = item*item
print(d)

"""
Method 2 
 
d = {item:item*item for item in range(1,n+1)}
"""