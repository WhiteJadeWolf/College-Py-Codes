""" PYTHON PROGRAM TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE """

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("Before Swap :-- a =",a," b =",b)
a=a+b
b=a-b
a=a-b
print("After Swap :-- a =",a," b =",b)