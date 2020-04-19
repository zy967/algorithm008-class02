class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n:int) -> None:
        """
        In this question, we may use three pointers to save space:
        p1 point to the most-left un-mergered nums1 element
        p2 point to the most-left un-mergered nums2 element
        pw point to the most-left avaliable place to write for merging
        """
        p1, p2, pw = m-1, n-1, m+n-1
        while p1 >=0 and p2>= 0:
            if nums1[p1] > nums2[p2]:
                nums1[pw] = nums1[p1]
                p1 -= 1
            else:
                nums1[pw] = nums2[p2]
                p2 -= 1
            pw -= 1

        if p2 >= 0:
            nums1[:p2] = nums2[:p2]