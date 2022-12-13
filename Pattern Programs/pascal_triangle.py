n = 5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")

    print(" ".join(str(11 ** i)))