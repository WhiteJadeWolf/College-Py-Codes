""" Create a class "BankAccount" with attributes account number and balance. 
Implement methods to deposit and withdraw funds, and a display method to show the account details. """


class BankAccount:
    def __init__(self):
        self.accounts = {}

    def createacc(self, accno, name, bal=0):
        if accno in self.accounts:
            print("\nAccount already exists!")
        else:
            self.accounts[accno] = {'name': name, 'bal': bal}
            print("\nAccount created successfully.")

    def deposit(self, accno, amount):
        if accno in self.accounts:
            self.accounts[accno]['bal'] += amount
            print(f"\nDeposited {amount} successfully.\nNew Balance : {self.accounts[accno]['bal']}")
        else:
            print("\nAccount not found!")

    def withdraw(self, accno, amount):
        if accno in self.accounts and self.accounts[accno]['bal'] >= amount:
            self.accounts[accno]['bal'] -= amount
            print(f"\nWithdrew {amount} successfully.\nNew Balance : {self.accounts[accno]['bal']}")
        else:
            print("\nInsufficient funds or account not found!")

    def displayacc(self, accno):
        if accno in self.accounts:
            print(f"\nAccount Number : {accno}\nName : {self.accounts[accno]['name']}\nBalance : {self.accounts[accno]['bal']}")
        else:
            print("\nAccount not found!")


ba = BankAccount()
while True:
    choice = int(input("\n1 - Create New Account\n2 - Deposit\n3 - Withdraw\n4 - Display Account\n5 - Exit\nChoice : "))
    match choice:
        case 1:
            accno = input("Enter Account Number : ")
            name = input("Enter Name : ")
            bal = float(input("Enter Initial Balance : "))
            ba.createacc(accno, name, bal)
        case 2:
            accno = input("Enter Account Number : ")
            amount = float(input("Enter Amount to Deposit : "))
            ba.deposit(accno, amount)
        case 3:
            accno = input("Enter Account Number : ")
            amount = float(input("Enter Amount to Withdraw : "))
            ba.withdraw(accno, amount)
        case 4:
            accno = input("Enter Account Number : ")
            ba.displayacc(accno)
        case 5:
            break
        case _:
            print("INVALID INPUT - TRY AGAIN.")