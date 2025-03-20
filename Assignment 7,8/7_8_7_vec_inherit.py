""" Create a class for representing any 2-D point or vector. 
The methods inside this class include its magnitude and its rotation in degrees with respect to the X-axis. 
Using the objects define functions for calculating the distance between two vectors, dot product, cross product of two vectors. 
Extend the 2-D vectors into 3-D using the concept of inheritance. 
Update the methods according to 3-D. """

import math

class Vector2D:
    def __init__(self, r, theta):
        theta = math.radians(theta)  
        self.r = r
        self.theta = theta
        self.x = self.r * math.cos(self.theta)
        self.y = self.r * math.sin(self.theta)

    def dist(self, other):  
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):
        return (self.x * other.y) - (other.x * self.y) 

class Vector3D(Vector2D):
    def __init__(self, r, theta, phi):
        theta = math.radians(theta)  
        phi = math.radians(phi)      
        self.r = r
        self.theta = theta
        self.phi = phi
        self.x = r * math.sin(phi) * math.cos(theta)
        self.y = r * math.sin(phi) * math.sin(theta)
        self.z = r * math.cos(phi)

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        crossx = (self.y * other.z) - (self.z * other.y)
        crossy = (self.z * other.x) - (self.x * other.z)
        crossz = (self.x * other.y) - (self.y * other.x)
        return (crossx, crossy, crossz)

while True:
    choice = int(input("Enter your choice :--\n1 - 2D Vectors\n2 - 3D Vectors\n3 - Exit\nChoice : "))
    match choice:
        case 1:
            r1, t1 = map(float,input("Enter MAGNITUDE & THETA of 1st Vector : ").split())
            r2, t2 = map(float,input("Enter MAGNITUDE & THETA of 2nd Vector : ").split())
            vec1 = Vector2D(r1, t1)
            vec2 = Vector2D(r2, t2)
            dist = vec1.dist(vec2)
            dot = vec1.dot(vec2)
            cross = vec1.cross(vec2)
            print("\nDistance between the two vectors :",dist," units\nDot Product :",dot,"\nCross Prouct :",cross,"\n")
        case 2:
            r1, t1, p1 = map(float,input("Enter MAGNITUDE, THETA & PHI of 1st Vector : ").split())
            r2, t2, p2 = map(float,input("Enter MAGNITUDE, THETA & PHI of 2nd Vector : ").split())
            vec1 = Vector3D(r1, t1, p1)
            vec2 = Vector3D(r2, t2, p2)
            dist = vec1.dist(vec2)
            dot = vec1.dot(vec2)
            cross = vec1.cross(vec2)
            print("\nDistance between the two vectors : ",dist," units\nDot Product : ",dot,"\nCross Prouct : Vector",cross,"\n",sep='')
        case 3:
            break
        case _:
            print("INVALID INPUT - TRY AGAIN.")
            

