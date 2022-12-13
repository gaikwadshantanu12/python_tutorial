# Define a function to calculate & return sum of digits

def sumOfDigits(n):
    s = 0
    while(n != 0):
        r = n % 10
        s = s + r
        n = n // 10
    return s

print("Sum of digits =",sumOfDigits(1234))
