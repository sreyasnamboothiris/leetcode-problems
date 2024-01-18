class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        for i in s:
            a.append(i)
        b = set(a)
        return len(b)
