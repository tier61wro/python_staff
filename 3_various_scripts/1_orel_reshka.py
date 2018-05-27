#!/usr/bin/env python
import random
print ("start")
sum = 0
for i in range(1, 2):
    lots = round(random.random())
    #lots = random.randint(0, 1)
    #print ("i=",i,"lots = ",lots)
    sum += lots

if lots == 1:
    print ("YES")
else:
    print ("NO")

print ("sum=",sum)
