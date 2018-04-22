#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sys import argv

script_name, file_name_in = argv

print "file in  = ", file_name_in;

file_ob = open (file_name_in, 'r' )
fr = file_ob.read()
print fr
