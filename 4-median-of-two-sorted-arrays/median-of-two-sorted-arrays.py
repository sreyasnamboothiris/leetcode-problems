class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nam = nums1 + nums2
        n = len(nam)
        nam.sort()
        l = n/2
        s=0
        if n % 2 == 0:
            s = (nam[int(l)-1]+nam[int(l)])/2
        else:
            s = nam[int(l)]
        return s            
        