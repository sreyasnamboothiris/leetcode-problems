class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        ar = (nums[(len(nums)-1)]*nums[len(nums)-2]) - (nums[0]*nums[1])
        return ar