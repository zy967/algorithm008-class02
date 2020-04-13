#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] ç§»åŠ¨é›¶
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Solution 3:
        This solution has the idea of recording the position of most-left zero and swap it with the next non-zero number we meet.
        This algorithm makes sure that there is no non-zero number is behind any zero. Also, swaping numbers immediately keeps the
        order of the no-zero numbers.

        This solution has the similar performance comparing with solution 1, while the code is much more clear and elegant.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        """
        Solution 1:
        Remove all 0 and append them at the end of array
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # i = 0
        # length = len(nums)
        # counter = 0
        # while i < length:
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         length -= 1
        #         counter += 1
        #     else:
        #         i += 1
        # for c in range(counter):
        #     nums.append(0)

        """
        Solution 2:
        We are using a queue to record each position that a non-zero number can move forward and fill in.
        Each time we meet a zero, push it's postion(index) to queue.
        If we meet a non-zero number, it will be taken to the first position in queue,
        where the remained space filled by zero, and pushed in the queue.

        This solution actually takes more operation and Memories comparing to solution 1...
        However, this one is close to the idea of solution 3, which actually record only the head of queue and do the swap.

        Time Complexity: O(n)
        Space Complexity: O(n) Cause we need to record position of zeros, the worst case should equal to the total number of zero.
        """
        # avaliablePlaces = []
        # i = 0
        # length = len(nums)
        # while i < length:
        #     if nums[i] == 0:
        #         avaliablePlaces.append(i)
        #     else:
        #         if len(avaliablePlaces) > 0:
        #             nums[avaliablePlaces[0]] = nums[i]
        #             avaliablePlaces.pop(0)
        #             avaliablePlaces.append(i)
        #             nums[i] = 0
        #     i += 1

# @lc code=end

