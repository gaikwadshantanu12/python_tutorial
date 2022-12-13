class Duck:
    def talk(self):
        print("Quack Quack")

class Dog:
    def talk(self):
        print("Bow Bow")

class Cat:
    def talk(self):
        print("Meow Meow")

class Goat:
    def talk(self):
        print("Mhyaa Mhyaa")

def foo(obj):
    obj.talk()

list_obj = [Duck(), Dog(), Cat(), Goat()]

for obj in list_obj:
    foo(obj)