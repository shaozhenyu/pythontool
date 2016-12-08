def hammingWeight(n):
	num = 0
	while n != 0:
		if n%2 == 1:
			num += 1
		n = n/2

	print num

i = 0
for i in range(16):
	hammingWeight(i)
