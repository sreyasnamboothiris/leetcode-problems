class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        n=0
        nums.sort()
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if abs(nums[i] - nums[j]) <= nums[i]:
                    if nums[i]^nums[j] > n:
                        n = nums[i]^nums[j]
       

        return n

        