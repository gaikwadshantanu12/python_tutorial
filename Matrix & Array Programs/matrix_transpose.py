# WAP for transpose of matrix

r,c = [int(x) for x in input("\nEnter dimensions - ").split()]
m1 = [[int(x) for x in input("Row - %d : "%(i+1)).split()] for i in range(r)]
m2 = []

for i in range(c):
    a = [m1[j][i] for j in range(r)]
    m2.append(a)

print("Transpose - ",m2)