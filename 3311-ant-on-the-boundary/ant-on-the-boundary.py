class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ant = 0
        s = 0
        for i in nums:
            s+=i
            if s == 0:
                ant +=1
        return ant