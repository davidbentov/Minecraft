class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def info(self):
        print(self.name, self.age)


person1 = Person("petr", 10)
person1.info()