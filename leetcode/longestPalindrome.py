#!/bin/python

def longestPalindrome(s):
	l = []
	m = {}
	for i in range(len(s)):
		if s[i] not in m:
			m[s[i]] = 1
		else:
			m[s[i]] += 1

	length = 0
	flag = 0
	for (_, v) in m.items():
		if v%2 == 0:
			length += v
		elif v > 0:
			flag = 1
			length += v-1

	if flag == 1:
		length += 1
	return length


len = longestPalindrome("abccccdd")
