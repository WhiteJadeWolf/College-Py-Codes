""" You are a student in a class of 10. Your class teacher assigns you a task of entering the
names of all the students in the class. You finally want to display the names given the
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
names and display them. [Hint: Slicing works when you are selecting maximum characters] """

l=eval(input("List of all students in class : "))
print("Names of students in reverse (max 15 characters) :--")
for i in range(len(l)):
    l[i]=l[i][:15]
    print(l[i][::-1],end="  ")