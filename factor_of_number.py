#WAP to print factors of given number

num = int(input("Enter any number - "))
i = 1
print("Factors of ",num,"are -")
while i <= num:
    if num % i == 0:
        print(i, end = "\t")
    i += 1