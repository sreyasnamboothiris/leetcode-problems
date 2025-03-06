class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        di_ct = {}
        ar = []
        ar2 = []
        for item in grid:
            for i in item:
                if i in di_ct:
                    di_ct[i] += 1
                else:
                    di_ct[i] = 1
        
        n = len(grid) * len(grid)
        for i in range(1,n+1):
            if i not in di_ct:
                ar2.append(i)
            elif di_ct[i] > 1:
                ar.append(i)
        

            
        return ar + ar2

            
        