'''
напишите класс который будет имитировать банковский счет
при создании экземпляра класса должны инициализироваться:

    имя
    баланс
    история

должны быть методы:

    show_balance -  показывает текущую дату и сумму на счете
    deposit - заносит деньги на счет и пишет в историю
    show_history - показывает историю зачислений
'''
import time


class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f'{self._get_current_time()}: increased sum to {amount} dollars')

    def show_balance(self):
        print(self.balance)

    def show_history(self):
        for h in self.history:
            print(f"=== {h} ===")

    @staticmethod
    def _get_current_time():
        return int(time.time())

a = Account('Vasya')

print(a.name)
a.deposit(50)
a.deposit(100)
a.deposit(20)
a.show_balance()
a.show_history()