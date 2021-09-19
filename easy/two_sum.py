nums = [3,3]
target = 6
indices = []
i = 0

while i < len(nums) - 1:
	j = i + 1
	while j < len(nums):
		if nums[i] + nums[j] == target:
			indices.append(i)
			indices.append(j)
			print(indices)
		j += 1
	i += 1


