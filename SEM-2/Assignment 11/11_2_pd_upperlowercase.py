""" Write a Pandas program to convert all the string values to upper, lower cases in a given pandas series. 
Also find the length of the string values.
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog']) """

import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

us = s.str.upper()
ls = s.str.lower()
lens = s.str.len()
print("Uppercase :--\n", us, sep='')
print("\nLowercase :--\n", ls, sep='')
print("\nLength of strings :--\n", lens, sep='')