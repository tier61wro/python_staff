#!/usr/bin/env python3
'''
Question:
    Define a class which has at least two methods:
        getString: to get a string from console input
        printString: to print the string in upper case.
        Also please include simple test function to test the class methods.
'''
class Luna:
    r = 'default'
    def __init__(self):
        self.s = self.r
    def get_from_console(self):
        self.s = input ('input some str\n')
        print ("you entered = ",self.s)
    def print_str_up(self):
        print ("str_UPP =",self.s.upper())

my_obj = Luna()
my_obj.print_str_up()
my_obj.get_from_console()
my_obj.print_str_up()
