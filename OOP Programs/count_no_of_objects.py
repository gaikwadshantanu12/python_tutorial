# WAP to create and class and count number of objects of class, class variable demo

class Test:
    count = 0       # static or class variable

    def __init__(self):
        Test.count += 1

    def show_count(self):
        print("No of objects :",Test.count)
        # print("No of objects :",self.count)

a = [Test() for i in range(10)]
a[0].show_count()