class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        ar_n = 0
        l = 0
        for i in range(1,n+1):
            
            if i % m == 0:
                l += i
            else:
                ar_n += i
        su = ar_n - l
        print(ar_n,su,l)
        return ar_n - l
        
        
        