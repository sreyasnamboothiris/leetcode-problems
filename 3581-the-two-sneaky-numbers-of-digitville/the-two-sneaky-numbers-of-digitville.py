class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        a = []
        for i in nums:
            if i not in a:
                if nums.count(i) == 2:
                    a.append(i)
        return a
        