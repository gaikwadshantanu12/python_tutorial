# WAP to take input 10 numbers and multiply it by given number

a = [int(x) for x in input("Enter 10 integers - ").split()]
n = int(input("Enter the number to multiply - "))
i = 0
while i < len(a):
    a[i] = a[i]*n
    i += 1

print(a)