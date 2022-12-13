class Test:
    myclass = 45            # class / static variable
    def __init__(self):
        self.myinstance = 50        # instance / object level variable

    def myMethod(self):
        mylocal = 60        # local variable
        print("Local Variable :",mylocal)

    def show(self):
        print("Class Variable :",Test.myclass)
        print("Instance Variable :",self.myinstance)

t1 = Test()
t1.myMethod()
t1.show()