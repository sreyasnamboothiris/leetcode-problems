class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        new = []
    
        for j in nums:
            if j < pivot:
                new.append(j)

        for j in nums:
            if j == pivot:
                new.append(j)

        for j in nums:
            if j > pivot:
                new.append(j)

        return new

        