#WAP to count a digit in given number

n = int(input("Enter number - "))
num = n
d = int(input("Enter the digit to count in above number - "))
count = 0
while num != 0:
    rem = num % 10
    if rem == d:
        count = count + 1
    num = num // 10

print(d,"occurs",count,"time in",n)