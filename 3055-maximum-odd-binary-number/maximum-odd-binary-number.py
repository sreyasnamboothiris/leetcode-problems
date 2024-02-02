class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count('1')
        t = ''
        for i in range(len(s)):

            if i == len(s)-1:
                t+='1'
                c-=1
            elif c > 1:
                t+='1'
                c=c-1
            else:
                t+='0'
        return t



        
        