"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. What is the minimum number of moves required?

Input

The first input line contains an integer n: the size of the array.

Then, the second line contains n integers x1,x2,…,xn: the contents of the array.

Output

Print the minimum number of moves.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
5
3 2 5 1 7

Output:
5
"""
from sys import setrecursionlimit
setrecursionlimit(2000005)

if __name__=='__main__':
	n = input()
	s = input()
	mi = 0
	prev = 0
	for ch in s.split():
		d = int(ch)
		if d>=prev:
			prev = d
			continue
		else:
			mi += (prev-d)

	print(mi)

 
