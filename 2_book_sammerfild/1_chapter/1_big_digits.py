#Эта программа принимает число в виде аргумента командной
#строки и выводит его на экран, используя «большие» цифры.

#!/usr/bin/env python3

from sys import argv

One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*   *", "  *  ", " *    ", "*    ", "*****"]

#print (One);
#for p in One: print (p)
#for p in Two: print (p)

try:
    number_in = argv[1]
    prins ("you entered ", number_in);
except IndexError:
    print ("usage: ", argv[0], " some_digit\n")
