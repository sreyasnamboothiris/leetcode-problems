class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        du = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if heights[i] != du[i]:
                c += 1
        return c
        