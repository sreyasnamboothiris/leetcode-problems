class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = 0
        a = []
        n = set(nums)
        for i in n:
            s = nums.count(i)
            a.append(s)
        f = max(a)
        s = a.count(f)
        return s*f
            
            
        

            
        