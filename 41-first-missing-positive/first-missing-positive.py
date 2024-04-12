class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n=[x for x in nums if x>0]

        n=list(set(n))
        n.sort()
        for i in range(1,len(n)+1):
            if i != n[i-1]:
                return i

        return len(n)+1