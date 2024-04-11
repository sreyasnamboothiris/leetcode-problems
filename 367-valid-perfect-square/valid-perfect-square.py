class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if sqrt(num) == int(sqrt(num)):
            return True
        else:
            return False