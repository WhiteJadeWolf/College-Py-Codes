"""                               Bigger is Greater
Given a word w.
Rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w.

Input Format :--
The first line of inputs contains t, number of test cases. Each of the next t lines contains w.

Constraints :--
1 <= t <= 105
1 <= |w| <= 100
w will contain only lower-case English letters and its length will not exceed 100.

Output Format :--
For each test case, output a string lexicographically bigger than w in a separate line. 
In case of multiple possible answers print the lexicographically smallest one and if no answer exists, print no answer.

Sample Input :--
11
ab
bb
hefg
dhck
dkhc
lmno
dcba
dcbb
abdc
abcd
fedcbabcd

Sample Output :--
ba
no answer
hegf
dhkc
hcdk
lmon
no answer
no answer
acbd
abdc
fedcbabdc

Explanation :--
Testcase 1: There exists only one string greater than ab which can be built by rearranging ab. That is ba.
Testcase 2: Not possible to rearrange bb and get a lexicographically greater string.
Testcase 3: hegt is the next string (lexicographically greater) to hefg. """

def biggerisgreater(s):
    s = list(s)
    k = len(s) - 2
    while k >= 0 and s[k] >= s[k+1]:
        k -= 1
    if k == -1:
        return "no answer"
    l = len(s) - 1
    while s[l] <= s[k]:
        l -= 1
    s[k],s[l] = s[l],s[k]
    s[k+1:] = reversed(s[k+1:])
    return ''.join(s)
    
t=int(input())
l=[]
for i in range(t):
	l.append(input())
print()
for i in l:
	print(biggerisgreater(i))