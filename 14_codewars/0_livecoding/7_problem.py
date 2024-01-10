import codewars_test as test
import sys
import re

# не работает
def hungry_seven_my_no_re(arr):
    seven_place = eight_place = nine_place = None
    for i in range(len(arr) -1, -1, -1):
        print(i)
        if arr[i] == 9:
            # print("found 9")
            nine_place = i
        elif arr[i] == 8:
            eight_place = i
        elif arr[i] == 7:
            seven_place = i

        if seven_place and eight_place and nine_place:
            if (nine_place - eight_place) == 1 and (eight_place - seven_place) == 1:
                print("FOUND SEQ")

################## MY ANSWER
def replace_seq(str_in):
    num_str_fixed = re.sub(r'789', '897', str_in, 0)
    return (num_str_fixed)

def hungry_seven_my(arr):
    num_str = ''.join([str(num) for num in arr])
    while re.search("789", num_str):
        num_str = replace_seq(num_str)
    return [int(el) for el in num_str]


################### GPT answer

def replace_789_with_897(num_str):
    """Replace all occurrences of the sequence '789' with '897' in a string."""
    return re.sub('789', '897', num_str)

def hungry_seven(arr):
    """Replace all sequences of the form [7, 8, 9] in a list with [8, 9, 7]."""
    num_str = ''.join(map(str, arr))  # Использование map для преобразования чисел в строки
    while '789' in num_str:  # Проверка наличия подстроки '789'
        num_str = replace_789_with_897(num_str)
    return list(map(int, num_str))  # Использование map для преобразования строк в числа

#============================


numbers_list = [7,7,7,8,9]
res = hungry_seven(numbers_list)
print(f'res = {res}')

# sys.exit(0)


@test.describe("Static Tests")
def test_example():
    @test.it("Tests")
    def _():
        test.assert_equals(hungry_seven([7,8,9]), [8,9,7])
        test.assert_equals(hungry_seven([7,7,7,8,9]), [8,9,7,7,7])
        test.assert_equals(hungry_seven([8,7,8,9,8,9,7,8]), [8,8,9,8,9,7,7,8])
        test.assert_equals(hungry_seven([8,7,8,7,9,8]), [8,7,8,7,9,8])