


# class Product:
#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price 

#     def __str__(self):
#         return f"{self.name} стоит {self.price}"

#     def __add__(self, other):
#         return self.price + other.price

#     def __lt__(self, other):
#         return self.price < other.price

#     # def info(self):
#     #     return f"{self.name} стоит {self.price}"

# p1 = Product("Ноутбук", 1500)
# p2 = Product("Мышка", 1100)
# print(p1)
# print(p1 + p2)
# print(p1 > p2)


# class MathUtils:

#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def is_even(number):
#         return number % 2 == 0

# print(MathUtils.add(10, 50))
# print(MathUtils.is_even(10))


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, data_str):
        username, email = data_str.split(",")
        return cls(username.strip(), email.strip())

# user = User.from_string("Bob, bob@gmail.com")
# print(user.username)


# МАГ МЕТОД 

# Создать класс Студент артибуты имя оценка 
# __str__ → вывод Студент: Алишер, средний балл: 4.2
# __len__ возвращает количество оценок

# Статический метод
# Создай класс Converter
# celsius_to_fahrenheit(c)
# fahrenheit_to_celsius(f)
# F = C * 9/5 + 32
# C = (F - 32) * 5/9
# print(Converter.celsius_to_fahrenheit(0))   # 32
# print(Converter.fahrenheit_to_celsius(32))  # 0

# Классовый метод
# Создай класс User
# username 
# email
# переменную platform_name = "MySite"
# classmethod create_admin(cls, username)
# → создаёт пользователя с email вида
# username@admin.mysite.com


# class Robot:
#     def move(self):
#         print("Robot")

# class VacuumCleaner:
#     def clean(self):
#         print("Пылесос убирает")

# class RobotVacuum(Robot, VacuumCleaner):
#     pass

# r = RobotVacuum()
# r.clean()
# r.move()

class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

class C(A):
    def hello(self):
        print("C")

class D(B, C):
    def hello(self):
        C.hello(self)

d = D()
d.hello()
print(D.mro())