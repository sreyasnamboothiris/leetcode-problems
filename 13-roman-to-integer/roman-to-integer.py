class Solution:
    def romanToInt(self, s: str) -> int:
        c = {'I':1,"V":5,
            'X':10,'L':50,
            'C':100,'D':500,"M":1000}
        n = 0
        i = 0
        while i < len(s):

            if i < len(s) - 1:
                if s[i] + s[i+1] == 'IV':
                    n += 4
                    i += 2
                elif s[i] + s[i+1] =='IX':
                    n += 9
                    i += 2
                elif s[i] +s[i+1] == 'XL':
                    n += 40
                    i += 2
                elif s[i] + s[i+1] == 'XC':
                    n += 90
                    i += 2
                elif s[i] + s[i+1] == 'CD':
                    n += 400
                    i += 2
                elif s[i] + s[i+1] == 'CM':
                    n += 900
                    i += 2
                else:
                    n += c[s[i]]
                    i += 1
            else:
                n += c[s[i]]
                i += 1
        return n