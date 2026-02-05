


# class User:
#     def __init__(self, id: int, email: str):
#         self.id = id
#         self.email = email 
# 
#     def info(self):
#         return f"{self.id}, {self.email}"
# 
# user1 = User(1, "admin@gmail.com")
# print(user1.info())
# 
# # Создать Класс Админ с атрибутом эмайл, создать метод 
# # get_info_email который выводит ответ Admin email
# 
# class Admin:
#     def __init__(self, email):
#         self.email = email
# 
#     def get_info_email(self):
#         print("Admin email")
# 
# admin = Admin("admin@gmail.com")
# admin.get_info_email()


# class Animal:
#     def speak(self):
#         print("Животное издает звук!")
# 
# class Dog(Animal):
#     def speak(self):
#         print("Gav")
# 
# animal = Animal()
# animal.speak()
# dog = Dog()
# dog.speak()


class User:
    def __init__(self, name):
        self.name = name

class Student(User):
    def __init__(self, name, age):
        super().__init__(name)  
        self.age = age

student = Student("Bob", 17)
print(student.name)
print(student.age)

'''
Создать класс User с артирибутом email и методом 
get_info выводит печатает email

создать класс AdminUser наследует от класса User
get_info выводит печатает "Admin : email" '''

class User:
    def __init__(self, email):
        self.email = email

    def get_info(self):
        return f"Печатает email"

class AdminUser(User):
    def get_info(self):
        return ("печатает Admin : email ")

class Teacher(User):
    def get_info(self):
        return ("печатает Teacher : email ")

class Student(User):
    def get_info(self):
        return ("печатает Student : email ")

admin = AdminUser("1@gmail.com")
print(admin.get_info())

tacher = Teacher("Islam")
print(tacher.get_info())