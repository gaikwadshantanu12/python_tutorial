# WAP to create unit matrix of given size

# Method 1 - Single Level Comprehension
row , column = [int(x) for x in input("Enter Rows X Columns - ").split()]
m = []
for i in range(row):
    a = [1 for i in range(column)]
    m.append(a)

print(m)

# Method 2 - Two Level Comprhension
"""
row , column = [int(x) for x in input("Enter Rows X Columns - ").split()]
m = [[1 for j in range(column)] for i in range(row)]
"""