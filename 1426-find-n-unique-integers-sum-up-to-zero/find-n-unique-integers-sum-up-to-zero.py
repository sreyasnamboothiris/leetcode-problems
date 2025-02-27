class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = 0
        v = []
        if n%2 != 0:
            v.append(k)
            n = n-1
        for i in range(1,(n//2)+1):
            v.append(i)
            v.append(i*-1)
        return v

            
            


        