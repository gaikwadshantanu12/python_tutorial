# WAP to create and class and count number of objects of class, class(static) variable demo, class method demo

class Test:
    count = 0
    def __init__(self):
        Test.count += 1

    def show_object_using_instance_method(self):
        print("Number of objects",Test.count)

    @classmethod
    def show_object_using_class_method(cls):
        print("Number of objects",cls.count)

Test.show_object_using_class_method()
t = Test()
t.show_object_using_instance_method()
Test.show_object_using_instance_method(t)
Test.show_object_using_class_method()
t.show_object_using_class_method()