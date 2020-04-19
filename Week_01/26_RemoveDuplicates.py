class Solution:
    def removeDuplicates(self, nums: list) -> int:
        count= 0

        for j in range(1, len(nums)):
            if nums[j] != nums[count]:
                count += 1
                nums[count] = nums[j]

        return count+1