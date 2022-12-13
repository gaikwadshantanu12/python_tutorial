# WAP to calculate sum of digits through function
# 1. Without recursion
# 2. Through recursion
# Do not use ready made functions or modules

# Method 2

def sum_of_digits(n):
    if n == 0:
        return 0

    return (n % 10 + sum_of_digits(n//10))

num = int(input("Enter number : "))
print(f"Sum of digits of {num} =",sum_of_digits(num))
