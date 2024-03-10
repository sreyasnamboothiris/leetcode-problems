class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set()
        nums1.sort()
        nums2.sort()
        for i in nums1:
            for j in nums2:
                if i == j:
                    a.add(i)
                
        return a

        