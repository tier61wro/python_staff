#!/usr/bin/env python3
import codecs

file_name = 'out';
f = open ('out', 'r', encoding = 'cp1251')
cont = f.read();
print ("cont = ", cont)
#text.encode("cp1251").decode('cp1251').encode('utf8')
#cont_utf = cont.decode('cp1251').encode('utf8')
#print ("cont_dec = ", cont_utf)
f_dec = open ('out_dec', 'w', encoding = 'utf-8')
f_dec.write(cont)


#with codecs.open(file_name, "r",encoding='utf-8', errors='ignore') as fdata:
#    cont = fdata.read();
#    print ("cont = ", cont)
