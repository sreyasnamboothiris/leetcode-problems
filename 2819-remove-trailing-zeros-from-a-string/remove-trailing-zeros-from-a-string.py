class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        nam = num[::-1]
        nam1 = int(nam)
        nam = str(nam1)
        nam2 = nam[::-1]

        return nam2