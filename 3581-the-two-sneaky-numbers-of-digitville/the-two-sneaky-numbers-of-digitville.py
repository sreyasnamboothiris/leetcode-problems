class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        a = []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                a.append(i)
            else:
                d[i] = 1
        return a
        