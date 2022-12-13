# WAP to check if given number is Armstrong number or not

num = int(input("Enter the number - "))
n = num
sum = 0
while n != 0:
    rem = n % 10
    sum = sum + rem*rem*rem         #rem ** 3
    n = n // 10

if num == sum:
    print(num,"is Armstrong number")
else:
    print(num,"isn\'t a Armstrong number")