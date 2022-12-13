#WAP to find factorial of a given number

num = int(input("Enter number for factorial - "))
i = fact = 1
while i <= num:
    fact = fact * i
    i += 1

print("Factorial of",num,"is -",fact)