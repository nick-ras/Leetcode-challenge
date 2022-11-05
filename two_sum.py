class Solution(object):
	def twoSum(self, nums, target):
		self.nums = nums
		self.target = target
		list = []
		for idx1, val1 in enumerate(nums):
			for idx2, val2 in enumerate(nums):
				if (idx1 == idx2):
					continue;
				if(val1 + val2 == target):
					list.append(idx1)
					list.append(idx2)
					return(list)
num = [3,2,4]
target = 6
theclass = Solution()
print(theclass.twoSum(num, target))