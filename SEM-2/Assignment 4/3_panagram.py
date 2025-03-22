"""              Pangrams
Roy wanted to increase his typing speed for programming contests so, his friend advised him to 
type the sentence “The quick brown fox jumps over the lazy dog” repeatedly because it is a 
pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once)
After typing the sentence several times, Roy became bored with is. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format :--
Input consists of a line containing s.

Output Format :--
Output a line containing pangram if s is a pangram, otherwise output not pangram

Sample Input #00 :--
we promptly judged antique ivory buckles for the next prize

Sample Output #00 :--
panagram

Sample Input #01 :--
we promptly judged antique ivory buckles for the prize

Sample Output #01 :--
not pangram

Explanation :--
In the first test case the answer is pangram because the sentence contains all the letters. """

from string import ascii_lowercase
d=dict([(ch, 0) for ch in ascii_lowercase])
# for i in range(97,123):
# 	d[chr(i)]=0
str=input().lower()
for i in str:
	if i.isalpha():
		d[i]+=1
print()
if 0 in d.values():
	print("not panagram")
else:
	print("panagram")