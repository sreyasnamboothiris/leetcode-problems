class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        l = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] - nums[j] > 0:
                    for k in range(j+1,len(nums)):
                        nam = (nums[i] - nums[j])*nums[k]
                        if nam > l:
                            l = nam
        return l
        