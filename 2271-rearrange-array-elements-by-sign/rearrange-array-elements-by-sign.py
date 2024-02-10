class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ar = list(filter(lambda x:x >= 0,nums))
        ar1 = list(filter(lambda x:x < 0,nums))
        ar2=[]
        j = 0
        k = 0
        i=0
        for i in range(len(nums)):
            if i % 2 == 0:
                ar2.append(ar[j])
                j+=1
            else:
                ar2.append(ar1[k])
                k+=1
        return ar2
            
        