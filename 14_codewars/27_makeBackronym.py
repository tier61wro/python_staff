'''
kata link: https://www.codewars.com/kata/55805ab490c73741b7000064
points: 7 kyu
type: OOP
----
back·ro·nym
    An acronym deliberately formed from a phrase whose initial letters spell out a particular word or words,
    either to create a memorable name or as a fanciful explanation of a word's origin.

    "Biodiversity Serving Our Nation", or BISON

(from https://en.oxforddictionaries.com/definition/backronym)

Complete the function to create backronyms. Transform the given string (without spaces) to a backronym,
using the preloaded dictionary and return a string of words, separated with a single space (but no trailing spaces).

The keys of the preloaded dictionary are uppercase letters A-Z and the values are predetermined words, for example:

dictionary["P"] == "perfect"

"dgm" ==> "disturbing gregarious mustache"
"lkj" ==> "literal klingon joke"
----
бакроним это вот такая забавная штука
https://ru.wikipedia.org/wiki/%D0%91%D1%8D%D0%BA%D1%80%D0%BE%D0%BD%D0%B8%D0%BC
пример: ВУЗ - Вышла Удачно Замуж
AЗЛК - автомобиль заранее лишенный качества
задание немного долбанутое в плане того что у нас нет словаря соответствия букв словам
типа предполагается что оно есть, но мы его не видим, поэтому локально не пройдут тесты
мы должны написать функцию которая преобразует акроним в бакроним - предполагая что словарь для преобразований у нас есть
'''
import dictionary as dictionary

import codewars_test as test
#preloaded variable: "dictionary"

# def make_backronym(acronym):
#     backronym_array = []
#     for l in acronym.upper():
#         backronym_array.append(dictionary[l])
#     return ' '.join(backronym_array)

def make_backronym(acronym):
    return ' '.join([dictionary[l] for l in acronym.upper()])



test.assert_equals(make_backronym("dgm"), "disturbing gregarious mustache")
test.assert_equals(make_backronym("lkj"), "literal klingon joke")
test.assert_equals(make_backronym('interesting'), 'ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious','Output not as expected')
test.assert_equals(make_backronym('codewars'), 'confident oscillating disturbing eager weird awesome rant stylish','Output not as expected')
