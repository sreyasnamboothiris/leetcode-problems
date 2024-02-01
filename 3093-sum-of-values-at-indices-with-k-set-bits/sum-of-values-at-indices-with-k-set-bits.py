class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        j = 0
        for i in range(len(nums)):
            n = bin(i)
            b = str(n)
            if b.count('1')==k:
                j = j+nums[i]
        return j
        
            

        