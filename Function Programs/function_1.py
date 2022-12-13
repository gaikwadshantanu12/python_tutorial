# Positional / Required Argument

# WAP define a function to print following pattern
"""
*
* *
* * *
* * * *
* * * * *

No of rows and character are given as parameter
"""

def pattern(ch,n):
    for i in range(1,n+1):
        print(i*ch)

ch = input("Enter character to print - ")
n = int(input("Enter number of rows - "))
pattern(ch,n)
