"""
WAP to print following output -

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

print("Pattern No. 4",end="\n\n")
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=" ")

    print()
