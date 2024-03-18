class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        k = 1
        l = 0
        nm = str(n)
        for i in nm:
            k *= int(i)
            l += int(i)

        x = k - l
        return x
