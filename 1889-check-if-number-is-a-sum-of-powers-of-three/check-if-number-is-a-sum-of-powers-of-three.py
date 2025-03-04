class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        while True:
            if n == 0:
                return True
            else:
                k = int(n % 3)
                print(k)
                if k != 0 and k != 1:
                    print(k)
                    return False
                else:
                    n = n / 3