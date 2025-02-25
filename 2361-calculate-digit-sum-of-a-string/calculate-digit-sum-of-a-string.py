class Solution:
    def digitSum(self, s: str, k: int) -> str:
        

        while len(s) > k:
            j = []
            for i in range(0,len(s),k):
                j.append(s[i:i+k])
            l = ''
            for item in j:
                n = 0
                for i in item:
                    n += int(i)
                l+=str(n)
            s = l
        return s

