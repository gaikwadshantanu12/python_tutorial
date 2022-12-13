# WAP to calculate power of x^y by using for loop

x = int(input("Enter base - "))
y = int(input("Enter index - "))
power = 1

for i in range(y):
    power = power * x

print(f"{x} raised to {y} is {power}")