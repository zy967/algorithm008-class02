class Solution:
    def twoSum(self, nums, target):
        h = {}
        i = 0
        length = len(nums)
        while i <= length:
            n = target - nums[i]
            if n not in h:
                h[nums[i]] = i
            else:
                return [h[n], i]
            i += 1