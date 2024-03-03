class Solution:
    def minimumSum(self, num: int) -> int:
        n = []
        s = str(num)
        for i in range(len(s)):
            n.append(int(s[i]))
        n.sort()
        s1 = str(n[0])+str(n[2])
        s2 = str(n[1])+str(n[3])
        s3 = int(s1)+int(s2)
        return s3
        