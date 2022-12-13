#WAP to find product of digits of given number

pro = 1
n = int(input("Enter number - "))
num = n
while num != 0:
    rem = num % 10
    pro = pro * rem
    num = num // 10

print("Product of digits of",n,"is",pro)