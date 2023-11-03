'''
train_date: 15.05.2022
kata link: https://www.codewars.com/kata/559e5b717dd758a3eb00005a
points: 7 kyu
type: REGEXP
-------------
DESCRIPTION:
DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase,
just like you see in the newspaper.

But for a change, let"s do that for each and every word of the given String.
Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.

*should work also on Leading and Trailing Spaces and caps

"apple"            => "Apple"
"apple of banana"  => "Apple of Banana"
"one   space"      => "One   Space
"   space WALK   " => "   Space Walk   "
-------------
TRANSLATION:

вам нужно написать функцию которая берет строку и если слово в ней длинее чем 2 символа, то мы делаем так что Первый символ
слова становится с большой буквы а остальные с маленькой, если слово меньше двух символов - то оставляем как есть его
-------------

===TRAINED====
функция
lower, title

красота:
def drop_cap(str_):
    return ' '.join( w.capitalize() if len(w) > 2 else w for w in str_.split(' ') )

TODO:
понять почему работает вотэто
def drop_cap(str_):
    return re.sub(r'\w{3,}', lambda x: x[0].title(), str_)
-------------
'''
import codewars_test as test


# def drop_cap(str_in):
#     words_out = []
#     for w in str_in.split(' '):
#         if len(w) > 2:
#             words_out.append(w.lower().title())
#         else:
#             words_out.append(w)
#     return ' '.join(words_out)

import re

def drop_cap(str_in):
    return re.sub(r'\w{3,}', lambda x: x[0].title(), str_in)

r = drop_cap('APPle Banana')
# r = drop_cap('YCLQ UZ tryoFJy')
# r = drop_cap('Qs')
print(r)
#===TESTS====

test.assert_equals(drop_cap('Apple Banana'),"Apple Banana")
test.assert_equals(drop_cap('Apple'),"Apple")
test.assert_equals(drop_cap(''),"")