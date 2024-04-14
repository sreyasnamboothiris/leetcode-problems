class Solution:
    def scoreOfString(self, s: str) -> int:
        k = 0
        for i in range(len(s)):
            if i < len(s)-1:
                b = abs(ord(s[i]) - ord(s[i+1]))
                k += b
        return k
        
            