class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        p_i = {}

        for i,num in enumerate(nums):
            if target - num in p_i:
                return [i,p_i[target-num]]
            p_i[num] = i
        