class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return int(len(candyType)/2) if len(candyType)/2<len(set(candyType)) else len(set(candyType))