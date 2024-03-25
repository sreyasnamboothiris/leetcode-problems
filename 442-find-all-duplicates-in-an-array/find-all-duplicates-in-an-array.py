class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        k = []
        nums.sort()
        for i in range(len(nums)):
            if i < len(nums)-1:

                if nums[i]==nums[i+1]:
                    k.append(nums[i])
        return k
        