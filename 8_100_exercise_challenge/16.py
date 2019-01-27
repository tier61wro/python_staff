#!/usr/bin/env python3
'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
str_in  = list(str(input('insert comma separated string in\n')).split(','))
str_out = [x for x in str_in if (int(x)%2 == 1)]
print (','.join(str_out))
