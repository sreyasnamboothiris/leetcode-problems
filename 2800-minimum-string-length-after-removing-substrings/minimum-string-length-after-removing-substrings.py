class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        while 'AB' in s or 'CD' in s:
            if 'AB' in s or 'CD' in s:
                s = s.replace('AB','').replace('CD','')
            
        return len(s)
        

                    
       


        