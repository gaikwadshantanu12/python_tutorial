# WAP to create list of all squares of integers from 1 to 10

# List Comprehension demo
l = [x*x for x in range(1,11)]
print(l)


"""
Working of above code - 

a = []
for x in range(1,11):
    a.append(x*x)
    
print(a)
"""