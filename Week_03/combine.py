class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(l, combo):
            if len(combo) == k:
                res.append(combo)
                return
            elif n - l < k - len(combo):
                return
            for i in range(l, n):
                helper(i+1, combo+[i+1])
        res = []
        helper(0, [])
        return res 
