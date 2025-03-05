class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left = []
        right = []
        center = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                center.append(i)
        return left + center + right

        