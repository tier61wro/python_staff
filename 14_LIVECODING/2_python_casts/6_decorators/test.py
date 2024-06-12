# class Foo:
#     def bar(self, x):
#         print(x)
#
#     def bar(self, x, y):
#         print(x, y)
#
# x = 2
# Foo().bar(x)

# например мы хотим получить квадраты всех чисел из массива используя map()
def exponentiation(n):
    return n * n

numbers = (1, 2, 3, 4)

result = map(exponentiation, numbers)
print(list(result))
# [1, 4, 9, 16]

# так же такие вещи можно делать сочетанием лямбда и map
result_lambda = map(lambda x: x*x, numbers)
print(list(result_lambda))

math_degree = [2, 2, 3, 3]

result_lambda_xy = map(lambda x, y: x ** y, numbers, math_degree)

print(list(result_lambda_xy))

l = [1, 2, 3, 4]
test = list(map(str, l))
print(test)