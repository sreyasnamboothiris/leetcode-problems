class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left = []
        right = []
        for i in range(len(nums)-1):
            if i - 1 >= 0:
                r = left[len(left)-1] + nums[i]
                left.append(r)
            else:
                left.append(0)
                left.append(nums[i])
        l = []
        k = sum(nums)
        for i in nums:
            f = k - i
            right.append(f)
            k = k-i
        print(right)
        for v in range(len(nums)):
            if len(nums) == len(left) == len(right):
                h = abs(left[v] - right[v])
                l.append(h)
            else:
                return [0]
        return l
        
        
        


        