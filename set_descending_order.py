# WAP to accept set as input and print elements in descending order.

s = eval(input("Enter set in {} - "))
print("Original Set - ",s)
print(sorted(s,reverse=True))

"""
Method 2 
s = eval(input("Enter set in {} - "))
for x in sorted(s,reverse=True):
    print(x,end='\t')
    
    
Method 3
print('Enter elements')
s = {int(x) for x in input().split()}
for x in sorted(s, reverse=True):
    print(x,end='\t')
"""