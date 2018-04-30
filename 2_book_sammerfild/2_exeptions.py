#!/usr/bin/env python

s = input ("enter some number ")

try:
    i = int(s)
    print ("Valid!")
except ValueError as er:
    print ("Oshibka:",er)
