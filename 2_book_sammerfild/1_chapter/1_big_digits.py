#Эта программа принимает число в виде аргумента командной
#строки и выводит его на экран, используя «большие» цифры.

#!/usr/bin/env python3

from sys import argv

One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*   *", "  *  ", " *    ", "*    ", "*****"]

#print (One);
for p in One: print (p)
for p in Two: print (p)

try:
    number_in = argv[1]
    print ("you entered ", number_in);
    if 2 >= int(number_in) >= 1:# change for regexp
        print ("Number is ok");
    else:
        print ("Number is bad");
except IndexError:
    print ("usage: ", argv[0], " some_digit\n")
