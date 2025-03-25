class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = {}
        for i in nums:
            n[i] = n.get(i,0)+1
        
        ar = [i for i in n if n[i]>1]

        return ar

            


        