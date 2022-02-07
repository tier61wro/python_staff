# модули нужные нам для того чтобы принтить дату
from datetime import datetime
import pytz


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    # зачисление на счет
    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, pytz.utc.localize(datetime.utcnow())])

    # снятие со счета
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'You spent {amount} units')
            self.history.append([-amount, pytz.utc.localize(datetime.utcnow())])
        else:
            print('Not enough money')
        self.show_balance()

    def show_balance(self):
        print(f'Balance = {self.balance}')

    def show_history(self):
        for s, d in self.history:
            print(f'sum_change: {s}, date: {d}')

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

# создаем экземпляр класса
a = Account('Oleg', 300)

a.show_balance()
