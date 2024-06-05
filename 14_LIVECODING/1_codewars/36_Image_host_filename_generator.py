
'''
train_date: 23.04.2022
kata link: https://www.codewars.com/kata/586a933fc66d187b6e00031a
points: 7 kyu
type: OOP
-------------
DESCRIPTION:

You are developing an image hosting website.
You have to create a function for generating random and unique image filenames.
Create a function for generating a random 6 character string which will be used to access the photo URL.
To make sure the name is not already in use, you are given access to an PhotoManager object.
You can call it like so to make sure the name is unique
// at this point, the website has only one photo, hosted on the 'ABCDEF' url
photoManager.nameExists('ABCDEF'); // returns true
photoManager.nameExists('BBCDEF'); // returns false

Note: We consider two names with same letters but different cases to be unique.

-------------
TRANSLATION:
вы должны создавать рандомные 6-ти значные уникальные имена для файлов на хостинге
на основе букв из string.ascii_letters
-------------
===TRAINED====
крутой пример на рекурсию
если имя не уникальное - то вызываем функцию еще раз

класс метод - метод класса который не принимает на вход экземпляр класса
-------------
'''

import codewars_test as test
from random import choice
import string


class photoManager(object):
    @classmethod
    def nameWasUnique(cls, name):
        return True


def generateName():
    random_str = "".join([choice(string.ascii_letters) for _ in range(6)])
    return random_str if photoManager.nameWasUnique(random_str) else generateName()


for i in range(10):
    name = generateName();

    test.expect(isinstance(name, str), "Name has to be a string.");
    test.expect(photoManager.nameWasUnique(name), "Name has to be unique.");
    test.assert_equals(len(name), 6, "Name has to be 6 digits long.");