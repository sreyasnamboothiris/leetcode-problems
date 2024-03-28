class Solution:
    def sortVowels(self, s: str) -> str:
        
        v = ['a','e','i','o','u','A','E','I','O','U']
        k = []
        n = ''
        c = 0
        for i in s:
            if i in v:
                k.append(ord(i))
        k.sort()
        for i in range(len(s)):
            if s[i] in v:
                n+=chr(k[c])
                c+=1
            else:
                n+=s[i]
        return n


        

