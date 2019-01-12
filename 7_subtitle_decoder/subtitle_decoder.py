#!/usr/bin/env python3
import codecs
import sys
import os

try:
    file_name = sys.argv[1]
except:
    print ("file name in")
    sys.exit(0)

try:
    f = open (file_name, 'r', encoding = 'cp1251')
except:
    print ("problem with file opening")
    sys.exit(0)


cont = f.read();
#print ("cont = ", cont)
f_out = os.path.join(os.path.dirname(file_name), 'decoded_' + os.path.basename(file_name))
print ("gonna save result in ", f_out)
f_dec = open (f_out, 'w', encoding = 'utf-8')
f_dec.write(cont)

if (os.path.isfile(f_out)):
    print ("OK: out file exists")
else:
    print ("ERROR: out file does't exists")

#with codecs.open(file_name, "r",encoding='utf-8', errors='ignore') as fdata:
#    cont = fdata.read();
#    print ("cont = ", cont)
