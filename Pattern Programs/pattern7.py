"""
WAP to print following pattern -

    *
   * *
  * * *
 * * * *
* * * * *

"""

print("Pattern No. 7",end="\n\n")
n = int(input("How many rows ? - "))
k = n - 1                                    #inital space count
for i in range(1,n+1):
    for j in range(k):                      #k is space count
        print(end=" ")
    for j in range(i):
        print("* ",end="")

    print()
    k = k - 1