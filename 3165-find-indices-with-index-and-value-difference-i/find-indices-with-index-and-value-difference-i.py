class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ar = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
                    ar.append(i)
                    ar.append(j)
        if len(ar)>0:
            return ar
        return [-1,-1]



