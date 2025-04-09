""" Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens according to the following constraints :--
a. Each row should have exactly only one queen.
b. Each column should have exactly only one queen.
c. No queens are attacking each other.

Write a program to place the queens randomly in the chess board so that all the conditions are satisfied. 
Find the solutions to the problem. """

import numpy as np

def checkvalidity(perm):
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if abs(perm[i] - perm[j]) == abs(i - j):
                return False
    return True

def random_solution():
    while True:
        perm = np.random.permutation(8)
        if checkvalidity(perm):
            return perm

def displayboard(perm):
    board = np.zeros((8, 8), dtype=int)
    for row, col in enumerate(perm):
        board[row, col] = 1  # 1 represents a queen
    return board

res = random_solution()
board = displayboard(res)

print(f"Random valid queen positions (row index = row, value = column) : {res}\n")
print("\nBoard representation (1 = queen) :-- \n", board)
