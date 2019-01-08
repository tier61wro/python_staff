#!/usr/bin/env python3
"""
>>> add(3,4)
7
"""
def add(a,b):
    return (a+b)
pi_short = 3.14
pi_long = 3.1415

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print ("all tests passed")
