#!/bin/python

def reverseBits(n):
	b = bin(n)
	b = b[2:]
	b = b[::-1]

	i = 32-len(b)
	while i > 0:
		b += "0"
		i -= 1

	return int(b, 2)

m = reverseBits(43261596)
print m
