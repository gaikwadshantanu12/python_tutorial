# WAP to sort a tuple by its float element
# Sample data : [('item1','12.20'),('item2','24.5'),('item3','15.10')]
# Expected Output : [('item1','12.20'), ('item3','15.10'), ('item2','24.5')]

a = [('item1','12.20'),('item2','24.5'),('item3','15.10')]
print(sorted(a,key = lambda x : float(x[1])))

# reverse parameter of sort set to false for descending order
# this is a built in function used above we can also used a.sort() method
