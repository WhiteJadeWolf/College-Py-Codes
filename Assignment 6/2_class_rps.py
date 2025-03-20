""" Write a class called Rock_paper_scissors that implements the logic of the game Rock-paper-scissors. 
For this game the user plays against the computer for a certain number of rounds.

Your class should have fields for the how many rounds there will be, the current round number, and the number of wins each player has. 
There should be methods for getting the computer's choice, finding the winner of a round, and checking to see if someone has won the (entire) game. 
You may want more methods. """

import random

class Rock_paper_scissors:

    def __init__(self, tr):  # tr - total rounds ; rn - round no. ; wc - win count list
        self.tr = tr
        self.rn = 0
        self.wc = []

    def round(self, choice):
        vessel = 'rps'
        gamekey = {'r':'p','p':'s','s':'r'} # which defeats which
        comp = vessel[random.randint(0,2)]  # computer's choice
        print("Computer's choice :",comp)
        if choice == gamekey[comp]:
            print("You win the round")
            self.wc.append(True)
            self.rn += 1                   # successful round updates rn but if comp == choice, then rn is not updated and round restarts
        elif comp == gamekey[choice]:
            print("You lost the round")
            self.wc.append(False)
            self.rn += 1
        print()

    def checkroundwin(self):
        check = int(input("Enter round no. to check win : ")) - 1
        return self.wc[check]
    
    def checkwin(self):
        if self.rn == self.tr :
            if self.wc.count(True) > self.tr // 2 :
                print("Congratulations ! You Won the Game !\n")
            elif self.wc.count(True) < self.tr // 2 :
                print("Sorry, you lost to computer !\n")
            else :
                print("Tie Game !")
        else :
            print("All rounds not completed yet\n")


tr = int(input("Enter total no. of rounds : "))
rps = Rock_paper_scissors(tr)
print()
while(rps.rn < rps.tr):
    choice = input("Enter your choice :--\nr - choose rock\np - choose paper\ns - choose scissors\nChoice : ")
    rps.round(choice)
if rps.checkroundwin():
    print("Round Won\n")
else:
    print("Round Lost\n")
rps.checkwin()

    


        


