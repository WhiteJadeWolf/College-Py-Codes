""" Write a program to implement the string split method without using predefined functions """

def SPLIT(str,separator=' ',maxsplit=-1):
    l=[]
    tempind,c,nstr,nx=0,0,0,0
    for i in str:
        nstr+=1
    for i in separator:
        nx+=1
    for i in range(nstr):
        if str[i+1:(i+1)+nx]==separator:
            l.append(str[tempind:i+1])
            c+=1
            tempind=(i+1)+nx
            if c==maxsplit:
                l.append(str[tempind:])
                return l
    l.append(str[tempind:])
    return l



    

# test
print(SPLIT("My course is AI"))
print(SPLIT("My course is AI",'c'))
print(SPLIT("Apple, Orange, Banana, Strawberry",", "))
print(SPLIT("Apple, Orange, Banana, Strawberry",", ",2))
print(SPLIT("Apple, Orange, Banana, Strawberry","x"))