class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        f = 2147483647
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    for k in range(j+1,len(nums)):
                        if nums[k]<nums[j]:
                            l = nums[i]+nums[j]+nums[k]
                            if l < f:
                                f = l
        if f == 2147483647:
            return -1
        else:
            return f