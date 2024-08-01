class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        ms = max(d.values())
        k = []
        for i in range(ms):
            ar = []
            for key,value in d.items():
                if value > 0:
                    ar.append(key)
                    d[key] = value - 1
                else:
                    pass
            k.append(ar)
        return k
            

            
            