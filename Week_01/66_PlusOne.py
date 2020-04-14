#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] ĺ ä¸
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i != -1:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    # digits.insert(0, 0)
                    # Improve the performance by inserting 1 at the front and return directly, since here must be the end of adding
                    digits.insert(0, 1)
                    return digits
                else:
                    i -= 1
            else:
                digits[i] += 1
                return digits

# @lc code=end

