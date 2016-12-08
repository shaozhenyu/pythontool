#!/bin/python

def intersection(nums1, nums2):
	nums1 = sorted(list(set(nums1)))
	nums2 = sorted(list(set(nums2)))

	nums = []
	i, j = 0, 0
	while i < len(nums1) and j < len(nums2):
		if nums1[i] == nums2[j]:
			nums.append(nums1[i])
			i += 1
			j += 1
		elif nums1[i] > nums2[j]:
			j += 1
		else:
			i += 1

	return nums

num1 = [4,7,9,7,6,7]
num2 = [5,0,0,6,1,6,2,2,4]
num = intersection(num1, num2)
print num
