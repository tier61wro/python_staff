class SensitiveValueAccess:
    def __init__(self):
        self._value = 10000

    def __get__(self, obj, type= None):
        print("LOG: sensitive variable was called")
        return (self._value)

class BankAccount:
    account = SensitiveValueAccess()

a = BankAccount()
print(a.account)