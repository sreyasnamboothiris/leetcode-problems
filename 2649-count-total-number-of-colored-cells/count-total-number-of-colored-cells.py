class Solution:
    def coloredCells(self, n: int) -> int:

        l = 1
        k = 0
        for i in range(n):
            l = k+l
            k = k+4
        return l
        