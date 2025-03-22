"""                                     Halloween Party
Alex is attending a Halloween party with his girlfriend Silvia. 
At the party, Silvia spots a giant chocolate bar. 
If the chocolate can be served as only 1*1 sized pieces and Alex can cut the chocolate bar exactly K times.
What is the maximum number of chocolate pieces Alex can cut and give Silvia?

Input Format :--
The first line contains an integer T, the number of test cases. T lines follow.
Each line contains an integer K.

Output Format :--
T lines. Each line contains an integer that denotes the maximum number of pieces can be obtained for each test case.

Constraints :--
1 <= T <= 10
2 <= K <= 107

Note :--
Chocolate must be served in size of 1*1 size pieces.
Alex can't relocate any of the pieces, not can he place any piece on top of other.

Sample Input #00 :--
4
5
6
7
8

Sample Output #00 :--
6
9
12
16                 

Explanation :--
The explanation below is for the first two test-cases. 
The rest of them follow a similar logic.
For the first test-case where K=5, You need 3 Horizontal and 2 Vertical cuts.
For the second test case where K=6, You need 3 Horizontal and 3 Vertical cuts.  """

t=int(input())
l=[]
for i in range(t):
    l.append(int(input()))
res=[]
for i in l:
    max=0
    for j in range(1,(i//2)+1):
        if j*(i-j)>max:
            max=j*(i-j)
    res.append(max)
print()
for i in res:
    print(i)