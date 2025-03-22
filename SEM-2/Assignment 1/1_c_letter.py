""" Create using for loop the list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z. """

x=[]
for i in range(1,27):
    x.append(i*(chr(96+i)))
print(x)