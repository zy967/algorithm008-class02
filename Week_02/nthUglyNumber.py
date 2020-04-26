class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = 1
        temp = 1
        dp2, dp3, dp5 = 0,0,0
        result = [1]*n
        while temp < n:
            result[temp] = min(result[dp2]*2, result[dp3]*3, result[dp5]*5)
            if result[dp2]*2 == result[temp]:
                dp2 += 1
            if result[dp3]*3 == result[temp]:
                dp3 += 1
            if result[dp5]*5 == result[temp]:
                dp5 += 1
            temp += 1
        return result[temp-1]
