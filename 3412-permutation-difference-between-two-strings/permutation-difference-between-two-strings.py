class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        m = 0
        for i in s:
            k = abs(s.index(i)-t.index(i))
            print(k,m)
            m += k
        return m
        