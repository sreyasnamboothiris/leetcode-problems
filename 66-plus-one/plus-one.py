class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = []
        l =""
        for i in digits:
            l += str(i)
        l=int(l)
        l+=1
        l=str(l)
        for i in l:
            k.append(int(i))
        return k


        