class Solution:
    def twoSum(self, nums, target):
        i = 0
        while i != len(nums):
            for index, number in enumerate(nums):
                if index != i:
                    if number + nums[i] == target:
                        return [i, index]
            i += 1
