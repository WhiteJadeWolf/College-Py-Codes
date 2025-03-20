""" Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
of the points in your 3-D space and store them in a list. The final output is a list with each
consisting of a point and its nearest neighbour. [Hint: Use distance between two points
formula] """

import math as m

def distance(x,y):
    dist=m.sqrt(m.pow((x[0]-y[0]),2)+m.pow((x[1]-y[1]),2)+m.pow((x[2]-y[2]),2))
    return dist

l=[]
res_list=[]
print("Input 10 points in 3-D plane :--")
for i in range(10):
    l.append(eval(input()))
for i in range(10):
    x=0
    minimum=0
    dist_list=[]
    for j in range(10):
        if i==j:
            continue
        else:
            dist_list.append(distance(l[i],l[j]))
    minimum=dist_list.index(min(dist_list))
    res_list.append((l[i],l[minimum]))
print("Resultant List :--",res_list)