""" Write a program to implement the string index method without using predefined functions """

def INDEX(x,str1,start=0,end=999999):
    str=str1[start:end]
    ns,nx=0,0
    for i in str:
        ns+=1
    for i in x:
        nx+=1
    for i in range(ns):
        if x==str[i:i+nx]:
            return i
    else:
        return("ValueError : substring not found")

# test
print(INDEX('a','cat'))
print(INDEX('bcd','abcde'))
print(INDEX('bcd','abcde',0,2))
print(INDEX('q','abcde'))
print(INDEX('bcd','abcde',0,4))