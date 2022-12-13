class MyClass:
    def __init__(self, a=None, b=None):         # default arguments
        if a != None and b != None:
            print("I got two parameters")
        elif a != None:
            print("I got one parameter")
        else:
            print("I got zero parameter(s)")

a1 = MyClass()
a2 = MyClass(10)
a3 = MyClass(10,20)