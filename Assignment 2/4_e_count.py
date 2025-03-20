""" Write a program to implement the string count method without using predefined functions """

def COUNT(x,str1,start=0,end=999999):
    str=str1[start:end]
    ns,nx,c=0,0,0
    for i in str:
        ns+=1
    for i in x:
        nx+=1
    for i in range(ns):
        if x==str[i:i+nx]:
            c+=1
    return c

# test
print(COUNT('a','cat'))
print(COUNT('bcd','abcde'))
print(COUNT('bcd','abcde',0,2))
print(COUNT('q','abcde'))
print(COUNT('bcd','abcde',0,4))
print(COUNT('e','abcdeee'))