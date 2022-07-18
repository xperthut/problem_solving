"""
A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input

The only input line contains an integer n.

Output

Print a beautiful permutation of integers 1,2,…,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106
Example 1

Input:
5

Output:
4 2 5 3 1

Example 2

Input:
3

Output:
NO SOLUTION
"""
from sys import setrecursionlimit
setrecursionlimit(2000005)

if __name__=='__main__':
	n = int(input())
	if n<5:
		if n==1:
			print(1)
		elif n==4:
			print(2,4,1,3)
		else:
			print('NO SOLUTION')
	else:

		m = n//2 if n%2==0 else 1+(n//2)
		i,j=1,m+1
		while i<=m:
			if i==m and n%2:
				print(i)
			else:
				print(i,end=' ')
			i+=1
			if j<=n:
				if j==n and n%2==0:
					print(j)
				else:
					print(j, end=' ')
				j+=1
	
		

