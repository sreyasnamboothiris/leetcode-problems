class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        k = []
        for i in bank:
            if i.count('1')>0:
                k.append(i.count('1'))
        t = 0
        for i in range(len(k)-1):
            t += k[i]*k[i+1]
        return t

                