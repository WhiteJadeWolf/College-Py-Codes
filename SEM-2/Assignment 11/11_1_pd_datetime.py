""" Write a Pandas program to create
a) Date time object for Jan 15 2012.
b) Specific date and time of 9:20 pm.
c) Local date and time.
d) A date without time.
e) Current date.
t) Time from a date time.
g) Current local time. """

import pandas as pd
from datetime import datetime

a = pd.Timestamp('2012-01-15')
print("DateTime object for Jan 15 2012 :", a)

b = pd.Timestamp('2012-01-15 21:20')
print("Specific date and time of 9:20 pm :", b)

c = pd.Timestamp.now()
print("Local date and time :", c)

d = pd.to_datetime('2025-04-09').date()
print("A date without time :", d)

e = pd.Timestamp.today().date()
print("Current date :", e)

f = pd.Timestamp.now().time()
print("Time from a date time :", f)

g = datetime.now().time()
print("Current local time :", g)
