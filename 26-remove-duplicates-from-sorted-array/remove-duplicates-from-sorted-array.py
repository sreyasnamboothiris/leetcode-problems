class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = set(nums)
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    nums.remove(nums[i])
                    nums.append(nums[i])
                    break
        return len(n)
        
        