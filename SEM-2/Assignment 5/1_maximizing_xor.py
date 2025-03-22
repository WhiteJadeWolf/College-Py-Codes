"""                                          Maximizing XOR
Given two integers: L and R.
Find the maximal values of A xor B.
Given, L <= A <= B <= R

Input Format :--
The input contains two lines, L is present in the first line. R in the second line.

Constraints :--
1 <= L <= R <= 103

Output Format :--
The maximal value as mentioned in the problem statement.

Sample Input #00 :--
1
10

Sample Output #00 :--
15

Sample Input #01 :--
10
15

Sample Output #01 :--
7

Explanation :--
In the second sample let's say L=10, R=15, then all pairs which comply to above condition are :--
10 xor 10 = 0
10 xor 11 = 1
10 xor 12 = 6
10 xor 13 = 7
10 xor 14 = 4
10 xor 15 = 5
11 xor 11 = 0
11 xor 12 = 7
11 xor 13 = 6
11 xor 14 = 5
11 xor 15 = 4
12 xor 12 = 0
12 xor 13 = 1
12 xor 14 = 2
12 xor 15 = 3
13 xor 13 = 0
13 xor 14 = 3
13 xor 15 = 2
14 xor 14 = 0
14 xor 15 = 1
15 xor 15 = 0
Here two pairs (10,13) and (11,12) have maximum xor value 7 and this is the answer.  """

l=int(input())
r=int(input())
max=0
for i in range(l,r+1):
    for j in range(i,r+1):
        if i^j>max:
            max=i^j
print("\n",max,sep='')