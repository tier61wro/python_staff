'''
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
----
разбить строку в массив по пробелу
text_arr = re.split(' ', text)
слепить строку пробелом
' '.join(encrypted_text_list)
'''
import re
import sys

import codewars_test as test


def encrypt_this(text):
    text_arr = re.split(' ', text)
    print(text_arr)

    for i, w in enumerate(text_arr):
        if len(w) > 1:
            w_arr = [*w]
            out_word = w_arr.copy()
            out_word[0] = str(ord(w_arr[0]))
            out_word[1], out_word[-1] = out_word[-1], out_word[1]
            text_arr[i] = ''.join(out_word)
        else:
            text_arr[i] = str(ord(w)) if w else ''
    str_out = ' '.join(text_arr)
    print(str_out)
    return str_out


def encrypt_this_gpt(word):
    if len(word) > 2:
        first_char_code = str(ord(word[0]))  # ASCII код первой буквы
        middle_chars = word[2:-1]  # Все символы между вторым и предпоследним
        encrypted = first_char_code + word[-1] + middle_chars + word[1]
    elif len(word) == 2:
        first_char_code = str(ord(word[0]))  # ASCII код первой буквы
        encrypted = first_char_code + word[-1]
    else:  # Для одного символа
        encrypted = str(ord(word)) if word else ''
    return encrypted


# Пример использования
encrypted_text = encrypt_this("Hello world")
print(encrypted_text)


text = "A wise old owl lived in an oak"
encrypt_this(text)



test.describe("Example Tests")

tests = [
    ("", ""),
    ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
    ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
    ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
    ("Why can we not all be like that wise old bird", "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
    ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
]

for t in tests:
    inp, exp = t
    test.assert_equals(encrypt_this(inp), exp)