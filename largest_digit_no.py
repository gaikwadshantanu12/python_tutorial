# WAP to find largest digit in given number

n = int(input("Enter the number - "))
largest = 0
num = n

while num != 0:
    rem = num % 10
    if rem > largest:
        largest = rem
    num = num // 10

print(largest,"is the largest number in",n)
