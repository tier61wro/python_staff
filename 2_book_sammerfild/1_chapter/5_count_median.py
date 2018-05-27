#!/usr/bin/env python3
#script finds median element - middle element, if odd list
#arithmetical mean of two middle numbers, if even list


import sys

#numbers = [5, 4, 3, 2, 1] # odd test list
numbers = [6, 5, 4, 3, 2, 1] # even test list

def find_max_el(a): # useless here
    len_a = len(a)
    print ("len =", len_a)
    max_el = 0
    for _ in range (len_a):
        if (a[_] > max_el):
             max_el = a[_]
        #print (a[_])
    return max_el;

def buble_sort(mylist):
    N  = len(mylist)
    print ("N = ", N)
    for j in range (1, N):
        print ("="*10)
        print ("j=", j)
        print ("mylist = ", mylist)
        for i in range (0, N - j):
            print ("i = ", i)
            if mylist[i] > mylist[i+1]:
                buf = mylist[i] 
                mylist[i] = mylist[i + 1]
                mylist[i + 1] = buf
    return mylist

#max_list = find_max_el(numbers)
sorted_list = buble_sort(numbers)
print ("sorted = ", sorted_list)
#sys.exit()

middle = int(len(numbers)/2)


if middle*2 == len(numbers): # even case
    print ("even list= ", numbers)
    med_el = (numbers[middle] + numbers[middle - 1 ])/2
else: #odd case
    print ("odd list= ", numbers)
    med_el = numbers[middle]
    
print ("Median = ",med_el)

