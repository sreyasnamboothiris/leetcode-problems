class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tr = []
        m = max(candies)
        for i in candies:
            if i + extraCandies >= m:
                tr.append(True)
            else:
                tr.append(False)

        return tr