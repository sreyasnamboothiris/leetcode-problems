class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        prime = [True for i in range(right+1)]
        p = 2
        prime_array = []
        if left < 2:
            left = 2
        while (p*p <= right):
            if prime[p] == True:
                for i in range(p*p,right+1,p):
                    prime[i] = False
            p += 1
        prime_array = [i for i in range(left, right + 1) if prime[i]]
        if len(prime_array) < 2:
            return [-1, -1] 
        min_diff = float('inf')
        result = [-1, -1]
        for i in range(1, len(prime_array)):
            diff = prime_array[i] - prime_array[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [prime_array[i - 1], prime_array[i]]

        return result
    

        