#WAP to print multiplication table of given number by using while loop

num = int(input("Enter number to print table - "))
i = 1
while i <= 10:
    print(num,"*",i,"=",num*i)          #print("%d * %d = %d"%(num,i,num*i))
    i += 1
