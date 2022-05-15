'''
train_date: 11.05.2022
kata link: https://www.codewars.com/kata/52eb114b2d55f0e69800078d
points: 6 kyu
type: OOP
-------------
DESCRIPTION:
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet,
where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"


-------------
TRANSLATION:
Шифр простой замены это шифр при котором в соответствии каждая буква заменяется другой буквой из альтернативного алфафита
ваша задача реализовать метод encode и decode.
Если в тексте который мы зашифровываем содержится буква которой нет в алфафите, то просто оставляем ее как есть
-------------
===TRAINED====
можно заменить через генератор
def encode(self, s): return ''.join([self.m2[self.m1.index(i)] if i in self.m1 else i for i in s])

а еще в питоне есть
вот такое:
translate(self.enc_key)
и вот такое
self.enc_key = str.maketrans(map1, map2)
-------------
'''

import codewars_test as test


class Cipher(object):
    def __init__(self, map1, map2):
        self.enc_dict = self.create_dict(list(map1), list(map2))
        self.dec_dict = self.create_dict(list(map2), list(map1))

    @staticmethod
    def code(s, code_dict):
        phrase_out = []
        for m in list(s):
            if m in code_dict:
                phrase_out.append(code_dict[m])
            else:
                phrase_out.append(m)
        return ''.join(phrase_out)

    def encode(self, s):
        return self.code(s, self.enc_dict)

    def decode(self, s):
        return self.code(s, self.dec_dict)

    @staticmethod
    def create_dict(l1, l2):
        res_dict = {}
        for i in range(0, len(l1)):
            res_dict[l1[i]] = l2[i]
        return res_dict

#===TESTS====
map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2)
test.assert_equals(cipher.encode("abc_"), "eta_");
test.assert_equals(cipher.encode("xyz"), "qxz");
test.assert_equals(cipher.decode("eirfg"), "aeiou");
test.assert_equals(cipher.decode("erlang"), "aikcfu");

map2 = 'tfozcivbsjhengarudlkpwqxmy';
cipher = Cipher(map1, map2);
test.assert_equals(cipher.encode('abc'), 'tfo');
test.assert_equals(cipher.decode('tfo'), 'abc');
test.assert_equals(cipher.decode('kjpphi'), 'tjuukf');
test.assert_equals(cipher.encode('ajqqtb'), 'tjuukf');
test.assert_equals(cipher.encode('a_bc&*83'), 't_fo&*83');