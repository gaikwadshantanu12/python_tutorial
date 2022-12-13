"""
WAP to print following output -

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

print("Pattern No. 6",end="\n\n")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")

    print()
