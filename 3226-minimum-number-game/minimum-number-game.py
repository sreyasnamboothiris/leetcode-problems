class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        aa = []
        b = int(len(nums)/2)
        for i in range(b):
            a=[]
            a.append(min(nums))
            nums.remove(min(nums))
            a.append(min(nums))
            nums.remove(min(nums)) 
            aa+=a[::-1]
        return aa      