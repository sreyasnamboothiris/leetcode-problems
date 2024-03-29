class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k=indices[:]
        for i in range(len(s)):
            k[indices[i]] = s[i]
        t = reduce(lambda x,y : x+y,k)
        return t
