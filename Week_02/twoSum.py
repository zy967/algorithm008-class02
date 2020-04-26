class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction={}
        for i,num in enumerate(nums):
            if diction.get(target - num) is not None:
                return [i,diction.get(target - num)]
            diction[num] = i
