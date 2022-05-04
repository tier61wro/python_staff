'''
train_date: 28.04.2022
kata link: https://www.codewars.com/kata/5a03af9606d5b65ff7000009/
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
-------------
TRANSLATION:
-------------
===TRAINED====
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
        if money_sum > other_user.balance or not other_user:
            raise ValueError
        self.balance += money_sum
        other_user.balance -= money_sum
        check = f'{self.name} has {self.balance} and {other_user.name} has {other_user.balance}.'
        return check

    def add_cash(self, money_sum):
        self.balance += money_sum
        return f'{self.name} has {self.balance}.'

#===TESTS====
@test.describe('Sample Tests')
def sample_tests():
    Jeff = User('Jeff', 70, True)
    Joe = User('Joe', 70, True)

    # test.assert_equals(Jeff.withdraw(122), 'Jeff has 68.')
    test.assert_equals(Joe.check(50), 'Joe has 120 and Jeff has 18.')
    test.assert_equals(Jeff.check(Joe, 80), 'Jeff has 98 and Joe has 40.')
    test.assert_equals(Jeff.add_cash(20), 'Jeff has 118.')