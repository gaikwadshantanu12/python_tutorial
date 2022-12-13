# WAP that takes a number as a parameter and check the number is prime or not

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:                # if no has extra factor
            return False

    return True

print(isPrime(int(input("Enter number to check prime or not : "))))
