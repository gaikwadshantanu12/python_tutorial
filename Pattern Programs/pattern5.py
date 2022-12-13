"""
WAP to print following output -

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

print("Pattern No. 5",end="\n\n")
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")

    print()
