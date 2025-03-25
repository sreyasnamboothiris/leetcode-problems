class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = {}
        ar = []
        for i in nums:
            if i in n:
                ar.append(i)
            else:
                n[i] = 1
        return ar

            


        