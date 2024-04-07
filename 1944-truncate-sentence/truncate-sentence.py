class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        p = s.split()
        l = ''
        for i in range(k):
            l += p[i]
            if i < k-1:
                l += ' '
        return l