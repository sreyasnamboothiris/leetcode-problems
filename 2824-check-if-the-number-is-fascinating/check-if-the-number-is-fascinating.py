class Solution:
    def isFascinating(self, n: int) -> bool:
        n1 = n*2
        n2 = n*3
        nam = str(n)+str(n1)+str(n2)
        for i in nam:
            if i == '0':
                return False
            if 1 < nam.count(i):
                return False
        return True
        