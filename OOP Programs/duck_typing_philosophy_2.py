class Duck:
    def talk(self):
        print("Quack Quack")

class Dog:
    def bark(self):
        print("Bow Bow")

def foo(obj):
    if hasattr(obj,"talk"):     # Method 1
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()

    """
    Or  # Method 2
    if type(obj) is Duck:
        obj.talk()
    elif type(obj) is Dog:
        obj.bark()    
    """

    """
    Or  # Method 3
    if isinstance(obj,Duck):
        obj.talk()
    elif isinstance(obj,Dog):
        obj.bark()    
    """

list_obj = [Duck(), Dog()]

for obj in list_obj:
    foo(obj)