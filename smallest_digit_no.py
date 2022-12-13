# WAP to find smallest digit in given number

n = int(input("Enter the number - "))
smallest = 9
num = n

while num != 0:
    rem = num % 10
    if rem < smallest:
        smallest = rem
    num = num // 10

print(smallest,"is the smallest number in",n)