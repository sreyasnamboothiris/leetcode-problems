class Solution:
    def reverseVowels(self, s: str) -> str:
        
        v = ['a','e','i','o','u','A','E','I','O','U']
        k = []
        ns = ''
        for i in s:
            if i in v:
                k.append(i)
        k.reverse()
        l = 0
        for i in s:
            if i in v:
                ns += k[l]
                l += 1
            else:
                ns += i
        return ns

