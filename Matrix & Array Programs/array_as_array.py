import array
a = [int(x) for x in input("Enter 10 integers - ").split()]
a = array.array('h',a)
print(a)