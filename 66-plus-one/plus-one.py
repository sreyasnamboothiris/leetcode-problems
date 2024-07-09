class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = ''
        for i in digits:
            k += str(i)
        m = int(k) + 1
        a = []
        for j in str(m):
            a.append(int(j))
        return a
        