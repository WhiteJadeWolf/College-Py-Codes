""" Write a program to make the length of each element 15 of a given Numpy array and the string centred, left-justified, right-justified with paddings of _ (underscore). 
Sample for testing : ['apple','bees','orange','peach','banana','hello'] """

import numpy as np

width = 15
pad = "_"
arr = np.array(eval(input(f"Enter a list of strings (size of each string <= {width}) : ")))
centered = np.array([s.center(width, pad) for s in arr])
leftpad = np.array([s.ljust(width, pad) for s in arr])
rightpad = np.array([s.rjust(width, pad) for s in arr])

print("Original strings :--\n", arr)
print("\nCentered :--\n", centered)
print("\nLeft-justified :--\n", leftpad)
print("\nRight-justified :--\n", rightpad)