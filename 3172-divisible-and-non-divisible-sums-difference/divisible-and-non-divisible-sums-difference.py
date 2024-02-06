class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        div = 0
        for i in range(1,n+1):
            if i % m == 0:
                div += i
            else:
                res += i
        s = res - div
        return s