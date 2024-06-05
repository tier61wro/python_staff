#9.05.2020
'''
Seven is a hungry number and its favourite food is number 9. Whenever it spots 9 through the hoops of 8, it eats it!
Well, not anymore, because you are going to help the 9 by locating that particular sequence (7,8,9) in an array of digits and tell 7 to come after 9 instead.
Seven "ate" nine, no more! (If 9 is not in danger, just return the same array)

    Test.assert_equals(hungry_seven([7,8,9]), [8,9,7])
    Test.assert_equals(hungry_seven([7,7,7,8,9]), [8,9,7,7,7])
    Test.assert_equals(hungry_seven([8,7,8,9,8,9,7,8]), [8,8,9,8,9,7,7,8])
    Test.assert_equals(hungry_seven([8,7,8,7,9,8]), [8,7,8,7,9,8])

-------
замена по $1, $2
str_list = re.sub(r'(7+)(89)', r'\2\1', str_list)
'''

import re

def hungry_seven(arr):
    str_list = ''.join(str(v) for v in arr)
    while re.search(r'(7+)(89)', str_list):
        str_list = re.sub(r'(7+)(89)', r'\2\1', str_list)
        print(str_list)
    return [int(x) for x in str_list ]

#seven_list = [7,8,9]
seven_list = [7,7,7,8,9]
seven_list = [8,7,8,9,8,9,7,8]
#seven_list = [8,7,8,7,9,8]

print(seven_list)
list_out = hungry_seven(seven_list)
print(list_out)
