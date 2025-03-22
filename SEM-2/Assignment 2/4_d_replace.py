""" Write a program to implement the string replace method without using predefined functions """

def REPLACE(str,old,new,count=-1):
    x=''
    c,ns,no,nn=0,0,0,0
    for i in str:
        ns+=1
    for i in old:
        no+=1
    for i in new:
        nn+=1
    j=0
    while(j<ns):
        if str[j:j+no]==old:
            x+=new
            j+=no
            c+=1
            if(c==count):
                x+=str[j:]
                break
        else:
            x+=str[j]
            j+=1
    return x

# test
print(REPLACE("My course is AI","AI","CSE"))
print(REPLACE("happy person",'p','t'))
print(REPLACE("america antarctica costa rica ",'ca ','#'))
print(REPLACE("america antarctica costa rica ",'ca ','#',2))
print(REPLACE("america antarctica costa rica ",'x','#'))