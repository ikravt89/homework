class SomeClass(object):
    attr = 41

    def method_1(self, x: int):
        print(2 * x)

obj = SomeClass()
obj.method_1(6)

print(obj.attr)

class Person:

    def __int__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name {self.name} Age: {self.age}")
