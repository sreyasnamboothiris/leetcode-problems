class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            k = s
        else:
            k = t
        for i in k:
            if s.count(i)!=t.count(i):
                return False
        return True
        