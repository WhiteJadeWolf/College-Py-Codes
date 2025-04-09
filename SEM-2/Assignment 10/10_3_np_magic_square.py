""" A magic square is an N x N grid of numbers in which the entries in each row, column and main diagonal sum to the same number (equal to N(N^2+1)/2). 
Create a magic square for N = 4, 5, 6, 7, 8 """

import numpy as np

def ms_odd(n):
    magic = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic[i, j] = num
        i2, j2 = (i - 1) % n, (j + 1) % n
        if magic[i2, j2]:
            i = (i + 1) % n
        else:
            i, j = i2, j2
    return magic

def ms_mod4(n):
    magic = np.arange(1, n * n + 1).reshape(n, n)
    idx = np.full((n, n), False)
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                idx[i, j] = True
    magic[idx] = (n * n + 1) - magic[idx]
    return magic

def ms_even(n):
    half_n = n // 2
    sub_square = ms_odd(half_n)
    magic = np.zeros((n, n), dtype=int)
    add = [0, 2, 3, 1] 
    for i in range(2):
        for j in range(2):
            magic[i*half_n:(i+1)*half_n, j*half_n:(j+1)*half_n] = \
                sub_square + (add[i*2 + j] * (half_n**2))
    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(n):
            if j < k or j >= n - k or (j == k and i == k):
                if j < half_n:
                    magic[i, j], magic[i + half_n, j] = magic[i + half_n, j], magic[i, j]
    return magic

def ms_generator(n):
    if n % 2 == 1:
        return ms_odd(n)
    elif n % 4 == 0:
        return ms_mod4(n)
    else:
        return ms_even(n)

for N in range(4, 9):
    print(f"\nMagic Square (N={N}) :--")
    square = ms_generator(N)
    print(square)
    print(f"Magic constant = {N * (N**2 + 1) // 2}")
