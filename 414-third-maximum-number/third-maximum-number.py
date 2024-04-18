class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        k = list(set(nums))
        k.sort(reverse=True)
        if len(k) > 2:
            return k[2]
        else:
            m = len(k)
            k.sort()
            return k[m-1]
          
        