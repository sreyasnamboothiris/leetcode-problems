class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a = [nums[0]]
        b = [nums[1]]
        for i in range(2,len(nums)):
            if b[len(b)-1] > a[len(a)-1]:
                b.append(nums[i])
            else:
                a.append(nums[i])
        return a+b

        
        