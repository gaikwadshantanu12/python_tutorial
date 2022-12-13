# WAP for addition of matrices

r,c = [int(x) for x in input("\nEnter dimensions - ").split()]
m1 = []
print("\n\nMatrix No 1")
for i in range(r):
    a = [int(x) for x in input("Row - %d : "%(i+1)).split()]           # single level comprehension
    m1.append(a)

print("\n\nMatrix No 2")
m2 = [[int(x) for x in input("Row - %d : "%(i+1)).split()] for i in range(r)]          # two level comprehension

m3 = []

# Without any comprehension
for i in range(r):
    a = []
    for j in range(c):
        a.append(m1[i][j] + m2[i][j])
    m3.append(a)

print("\n\nAddition - ",m3)

"""
Addition - 

Single Level Comprehension :- a = [m1[i][j] +m2[i][j] for j in range(c)]             #We have to write 'i' for loop

Two Level Comprehension :- m3 = [[m1[i][j] +m2[i][j] for j in range(c)] for i in range(r)]
"""

"""
Note - Same for Subtraction
"""