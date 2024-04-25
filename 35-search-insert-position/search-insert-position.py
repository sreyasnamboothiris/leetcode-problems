class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        s = False
        for i in range(len(nums)):
            if target <= nums[i]:
                s = True
                k = i
                break
        if s == False and k == 0:
            return len(nums)
        return k
