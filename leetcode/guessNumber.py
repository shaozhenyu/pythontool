def guess(n):
	if n == 6:
		return 0
	if n > 6:
		return 1
	else:
		return -1

def guessNumber(n):
	if guess(n) == 0:
		return n
	if guess(n) == 1:
		return twoSearch(n/2, n-1)
	else:
		return twoSearch(n+1, n*2)

def twoSearch(low, high):
	mid = (low + high)/2
	if guess(mid) == 0:
		return mid
	if guess(mid) == 1:
		return twoSearch(mid/2, mid-1)
	else:
		return twoSearch(mid+1, mid*2)

f = guessNumber(10)
print f
