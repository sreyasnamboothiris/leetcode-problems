class Solution:
    def isPalindrome(self, x: int) -> bool:

        
        k = str(x)
        b = k[::-1]
        print(b)
        if b==k:
            return True
        return False