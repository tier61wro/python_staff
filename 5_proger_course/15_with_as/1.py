#!/usr/bin/env python3

#Попробуйте самостоятельно открыть файл для записи и записать в него что-либо. Необходимо все сделать через менеджер With ... as.
with open('test_file', 'w+') as in_file:
    in_file.write("some important information\nsec_line")
    print ("Done")
f = open('test_file', 'r')
print ("f_cont  =---", f.read(),"---", end = '')
print ("======")
f.seek(0)
for line in f:
    print (line, end = '')
#print ("f_cont  =---", f.read(),"---",)


