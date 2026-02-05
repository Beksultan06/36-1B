


from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name 
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Возраст не может быть отрицательным!")

    @classmethod
    def create_from_year(cls, name, brith_year):
        age = datetime.now().year - brith_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return f"{self.name}, Age : {self.__age}"

class Emploee(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.position}, salary {self.salary}"

    def __add__(self, other):
        if isinstance(other, Emploee):
            return self.salary + other.salary
        return NotImplemented

class Driver:
    def __init__(self, license_number):
        self.license_number = license_number

    def drive(self):
        return f"Водитель {self.license_number} едет"

class Manager:
    def manager(self):
        return f"{self.name} упраляет командой"

class Director(Emploee, Driver, Manager):
    def __init__(self, name, age, position, salary, license_number):
        Emploee.__init__(self, name, age, position, salary)
        Driver.__init__(self, license_number)

    def __str__(self):
        return f"{self.name}, director salary {self.salary}, license {self.license_number}"

p1 = Person("Alice", 25)
p2 = Person.create_from_year("Bob", 1990)

e1 = Emploee("Islam", 30, "Engener", 8000)
e2 = Emploee("Norbolor", 25, "Front-End", 8000)

d1 = Director("Nursultan", 35, "MAin Director", 10000, "123qwe123")

print(p1.get_age())
# p1.set_age(-5)
p1.set_age(26)
print(p1.get_age())

print(e1)
print(e2)
print(e1 + e2)

print(Person.is_adult(17))
print(Person.is_adult(18))

print(d1)
print(d1.drive())
print(d1.manager())