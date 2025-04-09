""" The bisection method is a technique for finding solutions (roots) to equations with a single unknown variable. 
Given a polynomial function f, try to find an initial interval off by random probe. 
Store all the updates in an Numpy array. 
Plot the root finding process using the matplotlib/pyplot library. """

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x**2 - 4

np.random.seed(0)
found = False
while not found:
    a, b = np.random.uniform(-10, 10, 2)
    if f(a) * f(b) < 0:
        found = True
        if a > b:
            a, b = b, a
print(f"Initial interval  : a = {a:.4f}, b = {b:.4f}")

tolerance = 1e-6
max_iter = 100
updates = []
for i in range(max_iter):
    mid = (a + b) / 2.0
    updates.append(mid)
    if abs(f(mid)) < tolerance or (b - a) / 2 < tolerance:
        break
    if f(a) * f(mid) < 0:
        b = mid
    else:
        a = mid
updates = np.array(updates)
plt.figure(figsize=(10, 5))
x_vals = np.linspace(updates[0] - 1, updates[0] + 1, 400)
plt.plot(x_vals, f(x_vals), label="f(x)")
plt.axhline(0, color='gray', linestyle='--')
plt.plot(updates, f(updates), 'ro--', label="Bisection updates")
plt.title("Bisection Method Convergence")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
print(f"\nApproximate root after {len(updates)} iterations : x = {updates[-1]:.6f}")