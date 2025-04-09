""" Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
Store them in a numpy array. 
Convert them to polar coordinates. """

import numpy as np
N = int(input("Enter N (>=10) : "))
if N>=10:
    cart_pts = np.random.uniform(-10, 10, (N, 2))
    print("Cartesian Coordinates (x, y) :--\n", cart_pts)
    x = cart_pts[:, 0]
    y = cart_pts[:, 1]
    r = np.sqrt(x**2 + y**2) # r
    theta = np.arctan2(y, x) # theta
    pol_coords = np.column_stack((r, theta))
    print("\nPolar Coordinates (r, θ in radians) :--\n", pol_coords)
else:
    print("Wrong input. Run the program again\n")