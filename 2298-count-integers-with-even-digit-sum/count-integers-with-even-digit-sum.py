class Solution:
    def countEven(self, num: int) -> int:
        
        count = 0
        for i in range(2,num+1):
            k = []
            v = str(i)
            for j in v:
                k.append(int(j))
            
            print(k)
            c= 0
            for r in k:
                c+= r
            if c%2==0:
                count += 1
        return count

            
            