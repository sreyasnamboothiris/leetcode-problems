class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        k = 0
        for i in sentences:
            l = i.count(' ')
            if l > k:
                k = l
        return k+1