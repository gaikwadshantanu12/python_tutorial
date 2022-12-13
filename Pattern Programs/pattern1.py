"""
WAP to print following output -
*
* *
* * *
* * * *
* * * * *
"""

print("Pattern No. 1",end="\n\n")
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")

    print()
