class Solution:
    import sys

    sys.set_int_max_str_digits(100000)
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = []
        v = ''
        
        for i in range(len(num)-1,-1,-1):
            v = str(num[i]) + v
        s = int(v) + k
        s = str(s)
        for j in range(len(s)):
            l.append(int(s[j]))
        return l
        