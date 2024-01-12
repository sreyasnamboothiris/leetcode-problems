class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best =0
        i =1
        for i in range(1,int(len(s)/2)+1):
            b = ('0'*i+'1'*i)
            if b not in s:
                break
            best = i
        
        
        return best*2





