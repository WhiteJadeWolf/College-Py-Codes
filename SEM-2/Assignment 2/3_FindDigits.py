"""          Find Digits

You are given a number N, you need to print the number of positions where digits exactly 
divides N.

Input format ---
The first line contains T (number of test cases followed by T lines each containing N).

Constraints ---
1 <= T <= 15
0 <= N <= 1010

Output Format ---
For each test case print the number of positions in N where digits in that number exactly 
divides the number N in separate line.

Input ---
2
12
13

Output ---
2
1

Explanation---
Test case 1:
2 digits in the number 12 divides the number exactly.
Test case 2:
Only 1 digit in the number 13 divides the number exactly.
"""

t=int(input())
l=[]
for i in range(t):
	n=(input())
	c=0
	for j in n:
		if ((int(n))%(int(j)))==0:
			c+=1
	l.append(c)
print()
for i in l:
	print(i)		