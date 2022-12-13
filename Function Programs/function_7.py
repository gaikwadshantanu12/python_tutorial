# Define a function add which takes two integer parameters and return their addition

def add(num1, num2):
    return num1 + num2

x,y = [eval(i) for i in input("Enter two numbers : ").split()]
# print(add(10,20))

print("Addition =",add(x,y))

"""
x = [eval(i) for i in input("Enter two numbers : ").split()]

If we have one list and we have to pass each element of list as a separate paramter then :

print(add(*x))
"""