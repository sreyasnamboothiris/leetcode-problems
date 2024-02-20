class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = 0
        r = 0
        for i in nums1:
            if i in nums2:
                l+=1
        for i in nums2:
            if i in nums1:
                r+=1
        return [l,r]