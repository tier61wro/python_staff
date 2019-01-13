'''Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4],
 [0, 2, 4, 6, 8]
 ]

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
'''
import sys
str_in  = '3,5'
n,k = str_in.split(',')
print ("in params n={} k={}".format(n,k))

arr_out = [[0 for x in range(int(k))] for y in range(int(n))]

print ("arr_out = ", arr_out)
#sys.exit(0)
for i in range(int(n)):
#    print ("i =",i)
    for j in range(int(k)):
#        print ("j =",j)
        arr_out[i][j] = i*j

print ("arr_out = ", arr_out)
