#!/usr/bin/env python3
'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def check_odd_arr(arg):
    k = 0
    for i in arg:
        k = k + 1
        if (int(i) % 2) != 0:
            #print ("found not odd =", i)
            break
        elif (k == len(arg)):
            #print ("OK odd =", i)
            return 1
    return 0

for i in range (3, 20):
    d = list(str(i))
    if (check_odd_arr(d)) :
        print (i,',', sep = '', end = '')


