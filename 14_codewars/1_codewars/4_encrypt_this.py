'''
train_date: 5.05.2020
kata link: https://www.codewars.com/kata/5848565e273af816fb000449
points: 6 kyu
type: Fundamentals, strings
-------------
DESCRIPTION:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this kata.
Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter

Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"

re.split() #result = re.split(r'y', 'Analytics') результат:['Anal', 'tics']
-------------
TRANSLATION:
Зашифруй это!

Вы хотите создать секретные сообщения, которые можно будет расшифровать с помощью ката "Расшифруй это". Вот условия:

Ваше сообщение - это строка, содержащая слова, разделенные пробелами.
Вам нужно зашифровать каждое слово в сообщении, используя следующие правила:

Первая буква должна быть преобразована в ее ASCII-код.
Вторая буква должна быть поменяна местами с последней буквой.
Держим это простым: Во вводе нет специальных символов.
Примеры:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"

re.split() #result = re.split(r'y', 'Analytics') результат: ['Anal', 'tics']
-------------
===TRAINED====
разбить строку в массив по пробелу, лучше без re

слепить строку пробелом
' '.join(encrypted_text_list)

тернарный оператор в python

как узнать аски символ для буквы
'''


import re


def encrypt_this(text):
    text_arr = re.split(' ', text)
    encrypted_text_list = []
    for word in text_arr:
        if len(word) > 0:
            word_letters = [*str(word)]
            word_letters[0] = str(ord(word_letters[0]))
            if len(word) > 1:
                last = word_letters[-1]
                word_letters[-1] = word_letters[1]
                word_letters[1] = last
            encrypted_text_list.append(''.join(word_letters))

    return ' '.join(encrypted_text_list)


print(encrypt_this('Hello'))
print(encrypt_this('good'))
print(encrypt_this('hello world'))
print('---' + encrypt_this('') + '---')
print('---' + encrypt_this('k') + '---')
