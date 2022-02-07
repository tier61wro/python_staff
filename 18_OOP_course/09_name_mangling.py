# модули нужные нам для того чтобы принтить дату
from datetime import datetime
import pytz


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    # зачисление на счет
    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, pytz.utc.localize(datetime.utcnow())])

    # снятие со счета
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self._history.append([-amount, pytz.utc.localize(datetime.utcnow())])
        else:
            print('Not enough money')
        self.show_balance()

    def show_balance(self):
        print(f'Balance = {self.__balance}')

    def show_history(self):
        for s, d in self._history:
            print(f'sum_change: {s}, date: {d}')

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

# создаем экземпляр класса
a = Account('Oleg', 300)

a.show_balance()
