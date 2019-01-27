#!/usr/bin/env python3
'''
Question 17
Level 2
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
import re
total_sum = 0
tr_type = ''
summ = 0
while True:
    str_in = input('insert bank transaction record (D 100 or W 200)\n')
    if str_in:
        m = re.match(r"([DW]) (\d+)", str_in)
        if m :
            tr_type = m.group(1)
            summ = m.group(2)
            if tr_type:
                if tr_type == 'D':
                    total_sum += int(summ)
                elif tr_type == 'W':
                    total_sum -= int(summ)
                else :
                    continue
        else:
            print ("wrong format input data\n")
    else:
        print ("end of work")
        print ("total sum = %i" % total_sum)
        break
