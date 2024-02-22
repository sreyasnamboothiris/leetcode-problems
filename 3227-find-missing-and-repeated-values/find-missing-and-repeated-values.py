class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ar = [0,0]
        ma = len(grid)*len(grid)+1
        ka = False
        c=0
        for i in range(1,ma):
            ka = False
            c = 0
            for j in grid:
                for k in j:
                    if i == k:
                        ka = True
                        c+=1
                        print(c)
                        if c>1:
                            print(c)
                            ar[0] = i
                            break
            
                    
            if ka ==False:
                ar[1]=i
          

        return ar