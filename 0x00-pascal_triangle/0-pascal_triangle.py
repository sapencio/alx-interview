#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
	'''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
  '''
	a = [[] for i in range(n)]
	if type(n) is not int or n <= 0:
		return a
	for i in range(n):
		for j in range(i + 1):
			if (j < i):
				if (j == 0):
					a[i].append(1)
				else:
					a[i].append(a[i - 1][j] + a[i - 1][j - 1])
			elif (j == i):
				a[i].append(1)
	
	return a