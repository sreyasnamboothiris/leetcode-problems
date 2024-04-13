class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        for i in range(1,int(n/2)):
            if pow(4,i) == n:
                return True
            elif pow(4,i)>n:
                return False