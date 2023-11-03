'''
train_date: 28.04.2022
kata link: https://www.codewars.com/kata/5a03af9606d5b65ff7000009/
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
A company is opening a bank, but the coder who is designing the user class made some errors. They need you to help them.

You must include the following:
Note: These are NOT steps to code the class

    A withdraw method
        Subtracts money from balance
        One parameter, money to withdraw
        Raise a ValueError if there isn't enough money to withdraw
        Return a string with name and balance(see examples)

    A check method
        Adds money to balance
        Two parameters, other user and money
        Other user will always be valid
        Raise a ValueError if other user doesn't have enough money
        Raise a ValueError if checking_account isn't true for other user
        Return a string with name and balance plus other name and other balance(see examples)

    An add_cash method
        Adds money to balance
        One parameter, money to add
        Return a string with name and balance(see examples)

Additional Notes:

    Checking_account should be stored as a boolean

    No input numbers will be negative

    Output must end with a period

    Float numbers will not be used so, balance should be integer

    No currency will be used

Examples:

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

Jeff.withdraw(2) # Returns 'Jeff has 68.'

Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

Joe.check(Jeff, 100) # Raises a ValueError

Jeff.add_cash(20.00) # Returns 'Jeff has 118.'

-------------
TRANSLATION:
    # Joe.check(Jeff, 80) - Joe receives money from Jeff
    # other_user - отдает
-------------
===TRAINED====
если есть проверка на True переменной в if то можно делать вот так
if not other_user.checking_account or money_sum > other_user.balance:
ставя проверку на трушность на первое место
-------------
'''

import codewars_test as test


class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money_sum):
        if money_sum > self.balance:
            raise ValueError
        else:
            self.balance -= money_sum
        return f'{self.name} has {self.balance}.'

    def check(self, other_user, money_sum):
        if not other_user.checking_account or money_sum > other_user.balance:
            print(f"ALARM {money_sum} is more then {other_user.balance}")
            raise ValueError
        else:
            self.balance += money_sum
            other_user.balance -= money_sum
            check = f'{self.name} has {self.balance} and {other_user.name} has {other_user.balance}.'
            return check

    def add_cash(self, money_sum):
        self.balance += money_sum
        return f'{self.name} has {self.balance}.'


# ===TESTS====
@test.describe('Sample Tests')
def sample_tests():
    Jeff = User('Jeff', 70, False)
    Joe = User('Joe', 70, True)

    print(vars(Jeff))
    #
    # Joe.check(Jeff, 10)
    # print(vars(Jeff))
    # test.assert_equals(Jeff.withdraw(2), 'Jeff has 68.')
    # test.assert_equals(Joe.check(Jeff, 50), 'Joe has 120 and Jeff has 18.')
    # test.assert_equals(Jeff.check(Joe, 80), 'Jeff has 98 and Joe has 40.')
    # test.assert_equals(Jeff.add_cash(20), 'Jeff has 118.')
    # test.assert_equals(Joe.check(Jeff, 50), 'Joe has 120 and Jeff has 18.')
