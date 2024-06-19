class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k = set(nums)
        if len(k) == len(nums):
            return False
        else:
            return True
        