#8.05.2020
'''
Seven is a hungry number and its favourite food is number 9. Whenever it spots 9 through the hoops of 8, it eats it!
Well, not anymore, because you are going to help the 9 by locating that particular sequence (7,8,9) in an array of digits and tell 7 to come after 9 instead.
Seven "ate" nine, no more! (If 9 is not in danger, just return the same array)

    Test.assert_equals(hungry_seven([7,8,9]), [8,9,7])
    Test.assert_equals(hungry_seven([7,7,7,8,9]), [8,9,7,7,7])
    Test.assert_equals(hungry_seven([8,7,8,9,8,9,7,8]), [8,8,9,8,9,7,7,8])
    Test.assert_equals(hungry_seven([8,7,8,7,9,8]), [8,7,8,7,9,8])

-------
пройтись по индексам и элементам массива
for i, e in enumerate(list_in):
    print(f"i = {i}, e = {e}")
удалить i-й элемент массива
del seven_list[a]
мое решение похоже на:
https://www.codewars.com/kata/reviews/5e4bf6ad77d51a00011230c5/groups/5ea1f7db970cf100017d0fa5
но чето не проходили тесты
'''

def hungry_seven(arr):
    return arr

#seven_list = [7,8,9]
seven_list = [7,7,7,8,9]
#seven_list = [8,7,8,9,8,9,7,8]
#seven_list = [8,7,8,7,9,8]
print(seven_list)

def find_alarm(list_in):
    flag_7 = flag_8 = flag_9 = None
    for i, e in enumerate(list_in):
        #print(f"i = {i}, e = {e}")
        #print(f'flag7 = {flag_7}, flag8 = {flag_8}, flag9 = {flag_9}')
        if e == 7:
            flag_8 = None
            if flag_7 == None:
                flag_7 = i
        elif e == 8:
            if flag_7 != None:
                flag_8 = i
        elif e == 9:
            if flag_8:
                flag_9 = i
            else:
                flag_7 = None

        if flag_9:
            #print('need change')
            return flag_7, flag_9
    return

while find_alarm(seven_list):
    a, b  = find_alarm(seven_list)
    seven_list.insert(b+1, 7)
    del seven_list[a]
    #seven_list[a], seven_list[b] = seven_list[b], seven_list[a]



#print(f'a = {a}, b = {b}')
print(seven_list)


