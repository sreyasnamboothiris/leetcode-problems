class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        k = []
        p = words[0]
        for i in p:
            y = 1000
            for j in range(len(words)):
                g = words[j].count(i)
                print(g)
                if y > g:
                    y = g
                if y == 0:
                    break
            if y < 1000:
                if i not in k:
                    for c in range(y):
                        k.append(i)
        return k
                


