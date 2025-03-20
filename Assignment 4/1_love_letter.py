"""              The Love-Letter Mystery
James found a love letter his friend Harry has written for his girlfriend. 
James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follow 2 rules:
(a) He can reduce the value of a letter. 
E.g. He can change 'd' to 'c' but he cannot change 'c' to 'd'.
(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes 'a'. 
Once a letter has been changed to 'a', it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation.

Find the minimum number of operations required to convert a given string into a palindrome.

Input Format :--
The first line contains an integer T, i.e., the number of the test cases.
The next T lines will contain a string each.

Output Format :--
A single line containing the number of minimum operations corresponding to each test case.

Constraints :--
1 <= T <= 10
1 <= length of string <= 104
All character are lower case English letters.

Sample Input #00
:--
3
abc
abcba
abcd

Sample Output #01
:--
2
0
4

Explanation :--
For the first test case, ab*c* -> ab*b* -> aba.
For the second test case, abcba is a palindromic string.
For the third test case, abc*d* -> abc*c* -> abc*b* -> ab*c*a -> abba.

                """
def palmake(str):
	n=len(str)
	start,end,c=0,-1,0
	while(start<n//2):
		if(str[start]>str[end]):
			c+=(ord(str[start]))-(ord(str[end]))
		elif(str[end]>str[start]):
			c+=(ord(str[end]))-(ord(str[start]))
		start+=1
		end-=1
	return c

t=int(input())             
l=[]
for i in range(t):
	l.append(input())
print()
for i in l:
	print(palmake(i))

