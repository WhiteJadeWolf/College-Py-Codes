""" Write a class called Converter. 
The user will print("Length in inches :", self.length_in_m * 39.3701) a length and a unit when declaring an object from the class.
For example, c = Converter(9,'inches'). 
The possible units are inches, feet, yards, miles, kilometres, metres, centimetres, and millimetres. 
For each of these units there should be a method that returns the length converted into those units. 
For example, using the Converter object created above, the user could call c.feet(self) and should get 0.75 as the result. """

class Converter:

    def __init__(self, length, unit):
        self.d = {'inches':length/39.3701, 'feet':length/3.28084, 'yards':length/1.09361, 'miles':length*1609.34, 'kilometres':length*1000.0, 'metres':length*1.0, 'centimetres':length/100.0, 'millimetres':length/1000.0}       # covert respective units to metres
        self.length_in_m = self.d[unit]

    def inches(self):
        print("Length in inches :", self.length_in_m * 39.3701)

    def feet(self):
        print("Length in feet :", self.length_in_m * 3.28084)

    def yards(self):
        print("Length in yards :", self.length_in_m * 1.09361)

    def miles(self):
        print("Length in miles :", self.length_in_m / 1609.34)

    def kilometres(self):
        print("Length in kilometres :", self.length_in_m / 1000.0)

    def metres(self):
        print("Length in metres :", self.length_in_m / 1.0)

    def centimetres(self):
        print("Length in centimetres :", self.length_in_m / 100.0)

    def millimetres(self):
        print("Length in millimetres :", self.length_in_m / 1000.0)


u = input("Enter unit : ")
l = float(input("Enter length : "))
c = Converter(l,u)
c.inches()
c.feet()
c.yards()
c.miles()
c.kilometres()
c.metres()
c.centimetres()
c.millimetres()