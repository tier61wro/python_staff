'''
check if given string is in upper case
----
проверка того все ли буквы в заданной строке написаны в верхнем регинстре
тоесть по сути мы проверям не содержит ли строка букв в нижнем регистре
https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/solutions/python
----
тут решение через OOP
'''

class Word:
    def __init__(self, string=None):
        self.string = string
        self.small_letters = list(map(chr, range(ord('a'), ord('z')+1)))

    def is_upper(self):
        for i in self.string:
            if i in self.small_letters:
                return False
        return True


def is_uppercase(inp):
    a = Word(inp)
    return a.is_upper()

inp = 'Mama'
inp1 = 'MAMA MILA RAMU'

print(is_uppercase(inp))
print(is_uppercase(inp1))