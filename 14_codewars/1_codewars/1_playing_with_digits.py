"""
train_date: 02.05.2020
kata link: https://www.codewars.com/kata/5552101f47fc5178b1000050/
points: 6 kyu
type: FUNDAMENTAL, MATH
-------------
DESCRIPTION:
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

-------------
TRANSLATION:
Некоторые числа обладают забавными свойствами. Например:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2

46288 --> 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Дано положительное целое число n, записанное как abcd... (a, b, c, d... являются цифрами) и положительное целое число p.

Мы хотим найти такое положительное целое число k, если оно существует, что сумма цифр числа n, возведенных в последовательные степени p, равна k * n.
Другими словами:

Существует ли такое целое число k, что: (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k?

Если это так, мы вернем k, если нет, вернем -1.
-------------
===TRAINED====

-------------
распаковка массива, преобразуем цифры числа в массив
digits = [*str(n)]
-------------

"""


def dig_pow(n, p):
    digits = [*str(n)]
    sum = 0
    for d in digits:
        sum += int(d) ** p
        p += 1
    if sum % n == 0:
        return int(sum/n)
    return -1

res = dig_pow(695, 2)
