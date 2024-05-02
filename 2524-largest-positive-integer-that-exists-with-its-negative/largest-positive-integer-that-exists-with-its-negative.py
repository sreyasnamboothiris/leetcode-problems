class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l = -1
        for i in nums:
            if i < 0:
                if (i*-1) in nums:
                    if i*-1 > l:
                        l = i*-1
        return l
                    
        
        