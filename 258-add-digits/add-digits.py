class Solution:
    def addDigits(self, num: int) -> int:

        n = str(num)
        
        while len(n) > 1:
            k = 0
            for i in n:
                k += int(i)
            n = str(k)
        return int(n)