""" Create a class "Employee" with attributes name and salary. 
Implement overloaded operators + and - to combine and compare employees based on their salaries. """

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, second):
        return Employee(f"{self.name} & {second.name}", self.salary + second.salary)

    def __sub__(self, second):
        return abs(self.salary - second.salary)

    def __str__(self):
        return f"\nEmployees : {self.name}\nCombined Salary : {self.salary}"

while True:
    choice = int(input("\nEnter your Choice :--\n1 - Combine and Compare two employees' salaries\n2 - Exit\nChoice : "))
    match choice:
        case 1:
            name1 = input("Enter first employee's name : ")
            salary1 = float(input("Enter first employee's salary : "))
            name2 = input("Enter second employee's name : ")
            salary2 = float(input("Enter second employee's salary : "))
            emp1 = Employee(name1, salary1)
            emp2 = Employee(name2, salary2)
            print("\nCombined Employees :--", emp1 + emp2)
            print("Salary Difference :", emp1 - emp2)
        case 2:
            break
        case _:
            print("INVALID INPUT - TRY AGAIN")