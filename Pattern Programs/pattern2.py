"""
WAP to print following output -

* * * * *
* * * *
* * *
* *
*
"""

print("Pattern No. 2",end="\n\n")
for i in range(5,0,-1):
    for j in range(i+1,1,-1):
        print("*",end=" ")

    print()
