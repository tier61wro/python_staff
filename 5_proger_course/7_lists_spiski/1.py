#!/usr/bin/pythoin
l = [];
for i in range (1, 10):
    l.append(i)
l.clear()
l.append('33')
l.append('43')
l.append('23')

l.reverse()
l.sort()
print (l)
