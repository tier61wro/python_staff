#!/usr/bin/env pythoni3
'''Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
a = int(input("give me some number\n"))

#n2 = int( "%s%s%s" % (a,a,a) )

def create_concat_number(a,dlen):
    format_str = '';
    l = [];
    for i in range(1, dlen + 1):
        format_str = format_str + "%s"
        l.append(a)
    print ("format_str = ", format_str)
    t = tuple(l)
    n_fin = int( format_str % t)
    return n_fin

n_fin = create_concat_number(a, 1) + create_concat_number(a, 2) + create_concat_number(a, 3) + create_concat_number(a, 4)
print ("nfin = ", n_fin)
