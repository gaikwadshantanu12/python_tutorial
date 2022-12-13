# User defined function like filter

def myfilter(fn,ls):
    b = []
    for x in ls:
        if fn(x):
            b.append(x)

    return b

l = eval(input("Enter list in [] - "))
print(myfilter(lambda x:x%2==0,l))
