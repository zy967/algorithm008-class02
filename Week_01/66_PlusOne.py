class Solution:
    def plusOne(self, digits):
        i = len(digits) - 1
        while i != -1:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
                else:
                    i -= 1
            else:
                digits[i] += 1
                return digits