class Solution:
    def isHappy(self, n: int) -> bool:

        m = {}
        while True:
            li = list(str(n))
            j = 0
            for i in li:
                j += int(i)*int(i)
            if j in m:
                return False
            else:
                n = j
                m[j] = j
            if j == 1:
                return True
                
        