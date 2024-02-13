class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        s = ""
        for i in words:
            f = True
            for j in range(int(len(i)/2)):
                if i[j] != i[len(i)-j-1]:
                    f = False
                    break
            if f == True:
                s = i
                return s
        return s