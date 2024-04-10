class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k = 0
        
        for i in words:
            flag = True
            for j in i:
                if j not in allowed:
                    flag = False
                    break
            if flag:
                k += 1
        return k
        