#Эта программа принимает число в виде аргумента командной
#строки и выводит его на экран, используя «большие» цифры.

#!/usr/bin/env python3

from sys import argv
import re

Zero = ["  ***  "," *   * ","*     *","*     *","*     *"," *   * ","  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]

Digits = [Zero, One, Two]
#for p in One: print (p)

try:
    number_in = argv[1]
    print ("you entered ", number_in);
    row = 0
    while row < 7:
        line = ""
        curr_column = 0
        while curr_column < len(number_in):# column  -  порядковый номер числа во введенном числе
            #print ("we will draw %s part of %s" % (row,number_in[curr_column]))
            num = number_in[curr_column] #само текущее число
            arr_name  = Digits[int(num)] # тапл со заездочками соответствующий текущему числу
            str_tmp = arr_name[row] #часть тапла
            replaced = re.sub('\*', num, str_tmp) 
            line += replaced+"    "# формируем строку
            curr_column += 1
        print (line)
        row += 1
except IndexError:
    print ("usage: ", argv[0], " some_digit\n")
