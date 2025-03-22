"""                         Is Fibo
You are given a integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.
The first few elements of Fibonacci sequence are 0,1,1,2,3,5,8,13...... 
A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. 
The first two elements are 0 and 1.

Formally:--
Fib0 = 0
Fib1 = 1
Fibn = Fibn-1 + Fibn-2 for all n > 1

Input Format:--
The first lines contains T, number of test cases.
T lines follows. 
Each line contains an integer N.

Output Format:--
Display IsFibo if N is a fibonacci number and IsNotFibo if it is not a fibonacci number. 
The output for each test case should be displayed on a new line.

Constraints:--
1 <= T <= 10^5
1 <= N <= 10^10

Sample Input:--
3
5
7
8

Sample Output:--
IsFibo
IsNotFibo
IsFibo 

Explanation:--
5 is a fibonacci number given by Fib5 = 3 + 2
7 is not a fibonacci number
8 is a fibonacci number given by Fib6 = 5 + 3   """

def isfibo(n):
    a=0
    b=1
    while True:
        temp=b
        b=a+b
        a=temp
        if(n==b or n==0):
            return "IsFibo"
        elif(b>n):
            return "IsNotFibo"
    
t=int(input())
l=[]
for i in range(t):
    l.append(int(input()))
print()
for i in l:
    print(isfibo(i))