"""
WAP to check if given number is perfect number or not.

A number is perfect number if sum of its factor (other than itself) is equal to original number

For example - 6
                Factors of 6 - 1,2,3,6
                Note - Except 6
                Sum of its factor - 1 + 2 + 3 = 6
                Hence 6 is perfect number
"""

num = int(input("Enter any number - "))
sum = 0
i = 1
while i < num:
    if num % i == 0:
        sum = sum + i
    i += 1

if sum == num:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")