# Keyword Argument

# WAP define a function to print following pattern
"""
*
* *
* * *
* * * *
* * * * *

No of rows and character are given as parameter
"""

def pattern(ch='*',n=5):
    for i in range(1,n+1):
        print(i*ch)


pattern(n=5)            # keyword parameter only when if default values
