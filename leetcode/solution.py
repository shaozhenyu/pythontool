#!/bin/python

def moveZeroes(nums):
#	length = len(nums)
#	i = 0
#	num = 0
#	while i < length:
#		if nums[i] == 0 and i < length - num:
#			del nums[i]
#			nums.append(0)
#			num += 1
#		else:
#			i += 1
	nums.sort(key=lambda x:x==0)


nums = [0, 1, 0, 2, 0, 0, 4, 4, 4, 0]

moveZeroes(nums)
print nums
