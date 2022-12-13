# WAP to calculate sum of following series upto given terms
"""
1/1 + 2/2 + 3/4 + 4/8 + 5/16 + 6/32 + 7/64 + ............... + n
"""

n = int(input("Enter nth term - "))
sum = 0
y = 1

for x in range(1,n+1):
    sum = sum + x/y
    y = y * 2

print("Addition - ",sum)