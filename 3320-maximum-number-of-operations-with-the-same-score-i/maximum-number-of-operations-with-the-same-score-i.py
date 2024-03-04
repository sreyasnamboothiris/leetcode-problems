class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count = 0
        k = nums[0]+nums[1]
        for i in range(0,len(nums)-1,2):
            if nums[i]+nums[i+1]==k:
                count = count+ 1
            else:
                break
        return count
        