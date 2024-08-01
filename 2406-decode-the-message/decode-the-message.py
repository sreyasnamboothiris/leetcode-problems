class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s_c = {}
        l = 97
        key = key.replace(' ','')
        out = ''
        for i in key:
            if i in s_c:
                pass
            else:
                s_c[i] = chr(l)
                l += 1
        for i in message:
            if i == " ":
                out += " "
            else:
                out += s_c[i]
        return out
        
        