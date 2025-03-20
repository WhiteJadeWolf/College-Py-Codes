""" Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists. """

n=int(input("Enter length in feet : "))
l=[n*12,n/3.0,n/5280.0,n*304.8,n*30.48,n*0.3048,n*0.0003048]
c=int(input("Convert into :--\n1) inches\n2) yards\n3) miles\n4) millimeters\n5) centimeters\n6) meters\n7) kilometers\nChoice : "))
if c not in range(1,len(l)+1):
    print("Invalid Choice")
    quit
print("\n Result =",l[c-1])