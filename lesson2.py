



# class BankAccaunt:
#     bank_name = "Python Name"
# 
#     def __init__(self, owner, balance, password):
#         self.owner = owner 
#         self.account_type = "DEBIT"
#         self.__balance = balance
#         self.__password = password
# 
#     @property
#     def balance(self):
#         return self.__balance
# 
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             print("Error")
#         else:
#             self.__balance  =amount
#             print("Approved")
# 
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Пополнено {amount}")
#         else:
#             print("Сумма должно быть положительным!")
# 
#     def withdraw(self, amount, password):
#         if password != self.__password:
#             print("Password Error")
#             return 
# 
#         if amount > self.__balance:
#             print("Недостаточно")
#         else:
#             self.__balance -= amount
#             print(f"Снято {amount}")
# 
# account = BankAccaunt("Bob", 1500, '1234')
# print(account.owner)
# print(account.bank_name)
# 
# print(account.balance)
# account.balance = 2000
# print(account.balance)
# 
# account.deposit(100)
# print(account.balance)
# account.withdraw(300, "1234")
# print(account.balance)
# account.withdraw(300, "0000")
# print(account.balance)


# class PaymentMethod:
#     def pay(self, amount):
#         raise NotImplementedError("Метод pay() должен быть реализован!")

# class CardPAyment(PaymentMethod):
#     def pay(self, amount):
#         print(f"Оплата картой на сумму {amount}")

# class PayPalPayment(PaymentMethod):
#     def pay(self, amount):
#         print(f"Оплата через PayPal на сумму  {amount}")

# class CryptoPayment(PaymentMethod):
#     def pay(self, amount):
#         print(f"Оплата криптовалютой на сумму {amount}")

# def payment_def(payment_method, amount):
#     payment_method.pay(amount)

# payments = [
#     CardPAyment(), 
#     PayPalPayment(),
#     CryptoPayment()
# ]

# for payment in payments:
#     payment_def(payment, 100)


class Dog:
    def speak(self):
        print("Gav")

class Cat:
    def speak(self):
        print("May")

def make_sound(obj):
    obj.speak()

make_sound(Dog())
make_sound(Cat())