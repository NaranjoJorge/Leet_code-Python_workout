#Given an integer array nums sorted in non-decreasing order, 
#remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same.

#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4]
def removeDuplicates(nums):
	k = i = 0
	while i < len(nums) - 1:
		j = i + 1
		while j < len(nums):
			if nums[i] == nums[j]:
				nums.pop(j)
				continue
			j += 1
		i += 1
	for x in nums:
		k += 1
	return(k)