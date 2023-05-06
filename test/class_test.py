class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and I'm {} years old.".format(self.name, self.age))

person = Person("Alice", 25)
person.say_hello()