class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       
        a = []
        for i in nums:
            a.append(i*i)
        a.sort()
        return a
        