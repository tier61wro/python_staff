#!/usr/bin/env python3

'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import re
import json
let_dict = {}
sent_in = list(input('insert some sentence\n'))
for let in sent_in:
    if re.search(r"[A-Z]",let):
    	let_dict['capp'] = let_dict.get('capp', 0) + 1
    elif re.search(r"[a-z]",let):
    	let_dict['small'] = let_dict.get('small',0) + 1
    else :
    	let_dict['other'] = let_dict.get('other',0) + 1

j = json.dumps(let_dict, indent=4)
print (j)
