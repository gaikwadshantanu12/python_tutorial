# WAP using function to print a multiplication table

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

table(int(input("Enter number for table : ")))
