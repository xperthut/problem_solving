"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
"""
from sys import setrecursionlimit
setrecursionlimit(200005)

if __name__=="__main__":
	s = input()
	i,j=0,0
	mc = 0
	while j<len(s):
		if s[i]==s[j]:
			j+=1
			continue
		else:
			mc=max(mc, (j-i))
			i=j

	mc = max(mc, (j-i))

	print(mc) 


