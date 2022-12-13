"""
WAP to print following output -
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

print("Pattern No. 3",end="\n\n")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")

    print()
