class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = set(nums)
        for i in n:
            if nums.count(i)>2:
                return False
        return True
        