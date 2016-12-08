#!/bin/python

def isHappy(n):
	dic = {}

	m = 0
	while m != 1:
		m = 0
		while n != 0:
			m = m + (n%10) * (n%10)
			n = n/10
		if m not in dic:
			dic[m] = 1
		else:
			return False
		n = m
	return True

isHappy(19)
