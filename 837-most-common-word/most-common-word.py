class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        paragraph = re.sub(r'\W+', ' ', paragraph)
        
        k = paragraph.split()
        k = [word.lower() for word in k]
        banned = [word.lower() for word in banned]
        w = ''
        h = 0
        for i in k:
            
            if i not in banned:
                print(i)
                l = k.count(i)
                if l > h:
                    h = l
                    w = i
        return w

                

