class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        nam = 0
        lent = len(nums)
        for i in range(len(nums)):
            if lent % (i+1) == 0:
                nam += nums[i]*nums[i]
        return nam

