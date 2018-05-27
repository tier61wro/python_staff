#!/usr/bin/env python
from sys import argv

print ("start")

num_in = 7
if num_in < 10:
    print ("less then 10")
else: print ("more then 10")

countries = ['Norway', 'Sweden', 'Denmark']

for country in  countries:
    print ("contr=",country,"===")

s = input("enter num here: ")

try:
    i = int(s)
    print ("valid")
except ValueError as err:
    print (err)
##test comment
