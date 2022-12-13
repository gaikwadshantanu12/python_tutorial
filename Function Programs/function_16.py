# WAP that takes a list and returns new list with only numbers from given list

def numberList(a):
    b = []
    for x in a:
        if type(x) is int or type(x) is float:
            b.append(x)

    return b

print(numberList(eval(input("Enter list in [] : "))))

# replace with comprehension for block
"""
b = [x for x in a if type(x) is int or type(x) is float]

or

return [x for x in a if type(x) is int or type(x) is float]
"""