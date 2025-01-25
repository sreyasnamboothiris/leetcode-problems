class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        k = -1
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                if k < nums[i]:
                    return i
                    
        return k

        