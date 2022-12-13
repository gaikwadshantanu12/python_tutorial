# WAP to print following output

"""
A
A B
A B C
A B C D
A B C D E
"""



for i in range(1,6):
    count = ord('A')
    for j in range(i):
        print(chr(count),end=" ")
        count += 1
    print()