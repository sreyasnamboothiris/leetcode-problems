class Solution:
    def triangleType(self, nums: List[int]) -> str:


        nums.sort()
        if nums.count(nums[0])==3:
            return 'equilateral'
        elif nums[0]+nums[1] > nums[2] and nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return 'isosceles'
        elif nums[0]+nums[1] > nums[2]:
            return 'scalene'
        else :
            return 'none'
