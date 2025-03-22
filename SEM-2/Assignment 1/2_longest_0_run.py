""" Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros,
the largest number of zeros in a row. 
For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4. """

import random as r
l=[]
c=0
max=0
for i in range(100):
    n=r.randint(0,1)
    l.append(n)
    if(n==0):
        c+=1
        if(c>max):
            max=c
    else:
        c=0
print("Longest run of 0 =",max)
# print(l)