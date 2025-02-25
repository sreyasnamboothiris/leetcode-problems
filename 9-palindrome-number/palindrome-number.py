class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = 0
        m = x
        while m >= 1:
            v = m%10
            m = m//10
            s = v + (s * 10)
        print(s,x)
        if s == x:
            return True
        else:
            return False
            
                
    