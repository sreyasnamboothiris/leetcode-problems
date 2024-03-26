class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        a = 0
        for i in range(len(nums)):
            
            for j in range(len(nums)):

                if i == j:
                    pass
                else:
                    if nums[j]-nums[i] == diff:
                        for k in range(len(nums)):
                            if k != i or k != j:
                                if nums[k]-nums[j]==diff:
                                    a += 1
        return a