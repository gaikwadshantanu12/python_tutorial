#WAP to find sum of digits of given number

sum = 0
n = int(input("Enter number - "))
num = n
while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

print("Sum of digits of",n,"is",sum)