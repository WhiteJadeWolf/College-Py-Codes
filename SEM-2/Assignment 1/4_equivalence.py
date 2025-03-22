""" Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of numbers. 
Check the validity of your equivalence classes. 
[Hint: the union of all equivalence classes should be the original set/list.] """

limit=10000
modulo=5
l=[]
for i in range(modulo):
    l.append([])
for i in range(1,limit+1):
    l[i%modulo].append(i)
print("Equivalence Classes created successfully.")
print("Checking validity of equivalence classes...")
x=[]
for i in range(1,limit+1):
    x.append(i)
y=[]
for i in range(limit//modulo):
    for j in range(1,modulo+1):
        n=j%modulo
        y.append(l[n][i])
if x==y:
    print("Verified Successfully!")
else:
    print("Error")
#    print(x)
#    print(y)