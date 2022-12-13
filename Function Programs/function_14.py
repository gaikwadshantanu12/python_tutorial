# Create a function which prints :
# a) all prime numbers in given range
# b) all perfect numbers in given range     -       remain

def printPrime(start, end):
    if start > end:
        print("Invalid range")
        return

    for n in range(start,end+1):
        for i in range(2,n):
            if n % i == 0:
                break

        else:
            print(n,end=" ")


s,e = [int(i) for i in input("Enter range : ").split()]
print(f"Prime Number between {s} and {e}\n\n")
printPrime(s,e)
