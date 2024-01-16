class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr = []
        l = int(len(nums)/2)
        for i in range(l):
            arr.append(nums[i])
            arr.append(nums[l+i])
        return arr
        

        