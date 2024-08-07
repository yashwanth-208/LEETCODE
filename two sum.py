class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            rest = nums[i+1:]
            if (target - nums[i]) in rest: 
                return [i, i + 1 + rest.index(target-nums[i])]