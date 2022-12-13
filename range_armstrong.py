# WAP to print Armstrong number from 1 to 500

for n in range(1,501):
    t = n
    sum = 0
    while t != 0:
        r = t % 10
        sum = sum + r**3
        t = t // 10

    if sum == n:
        print(n,end="\t")