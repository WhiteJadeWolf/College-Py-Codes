""" PYTHON PROGRAM TO FIND THE FACTORIAL OF A NUMBER. """

m=1
n=int(input("Enter a number : "))
for i in range(n,1,-1):
    m*=i
print("Factorial =",m)