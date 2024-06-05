
# факториал
# 5! = 1*2*3*4*5, при этом факториал от 0 равен 1

import unittest

def fact(n: int) -> int:
    if n < 0:
        raise ValueError("must be greater 0")
    return 1 if n == 0 else n * fact(n-1)

res = fact(5)
print(res)


# фибоначи: сумма двух предыдущих
#f(0) = 1
#f(1) = 1
# f(n) = f(n-1) = f(n-2)
# 1 + 2 + 3 + 4



def fib(n: int)-> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < 0:
        raise ValueError("must be greater 0")
    else:
        return fib(n-1) + fib(n-2)


for i in range(1, 10):
    res = fib(i)
    print(res)


class TestFact(unittest.TestCase):
    def test_int_ok(self):
        self.assertEqual(fact(5), 120)

    def test_zero(self):
        self.assertEqual(fact(0),1)

    # def test_negative(self):
    #     with self.assertRaises(ValueError):
    #         fact(-1)
    def test_negative(self):
         with self.assertRaises(ValueError):
            fact(-1)

exit(0)
if __name__ == '__main__':
    unittest.main()