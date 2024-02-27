class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a=[]
        k = nums[0]
        for i in range(1,len(nums)):
            a.append(nums[i])
        a.sort()
        print(nums)
        k += a[0]
        k += a[1]
        return k
