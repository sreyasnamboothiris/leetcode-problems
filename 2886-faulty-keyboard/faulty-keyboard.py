class Solution:
    def finalString(self, s: str) -> str:
        r = ''
        for i in s:
            if i == 'i':
               r = r[::-1]
            else:
                r += i
        return r        
        