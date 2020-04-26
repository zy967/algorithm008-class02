class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = dict()
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in diction.keys():
                diction[tmp].append(i)
            else:
                diction[tmp] = [i]
        return list(diction.values())
