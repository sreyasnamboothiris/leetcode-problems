class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        one = []
        zero = []
        for i in nums:
            if i % 2 == 0:
                zero.append(0)
            else:
                one.append(1)
        return zero + one

        