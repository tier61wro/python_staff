#!/usr/bin/env python3
'''Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
 m = re.search(r"\d+", s)
'''
import re
letters = numbers = 0
str_in  = input ('insert some sentence\n')
symb_arr = list(str_in)
for s in symb_arr:
    print ("s=",s)
    if re.search (r"\d",s):
        #print ("found digit")
        numbers += 1
    elif re.search (r"[a-zA-Z]",s):
        #print ("found letter")
        letters += 1

print ("letters = ",letters, "numbers = ", numbers)
