# WAP to check whether a number is perfect or not

def isPerfectNumber(num):
    s = 0
    for i in range(1,num):
        if num % i == 0:
            s += i

    if num == s:
        return "Perfect Number"
    else:
        return "Not Perfect Number"

print(isPerfectNumber(int(input("Enter number to check perfect or not : "))))
