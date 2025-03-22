""" Write a class called Password_manager. 
The class should have a list called old_passwords that holds all of the user's past passwords. 
The last item of the list is the user's current pass word.
There should be a method called get_password that returns the current password and a method called set_password that sets the user's password. 
The set_password method should only change the password if the attempted password is different from all the user's past passwords.
Finally, create a method called is_correct that receives a string and returns a boolean True or False 
depending on whether the string is equal to the current password or not. """

class Password_manager:

    def __init__(self, old_passwords):
        self.old_passwords = old_passwords
    
    def get_password(self):
        return self.old_passwords[-1]
    
    def set_password(self, new_pass):
        if new_pass not in self.old_passwords:
            self.old_passwords.append(new_pass)
            self.current_pass = self.old_passwords[-1]
        else:
            print("Password not set : New password cannot be same as old ones")
    
    def is_correct(self, str):
        if str == self.old_passwords[-1]:
            return True
        else:
            return False
        
        
l = eval(input("Enter the password list : "))
passmgr = Password_manager(l)
print("Current password :",passmgr.get_password())
newpass = input("Enter new password : ")
passmgr.set_password(newpass)
curr = input("Enter your guess for current password : ")
print("Your guess is", passmgr.is_correct(curr))
