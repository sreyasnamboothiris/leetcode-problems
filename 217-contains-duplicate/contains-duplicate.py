class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ar1 = set(nums)
        if len(ar1)==len(nums):
            return False
        else:
            return True
        