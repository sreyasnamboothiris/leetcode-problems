class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in accounts:
            h = reduce(lambda x,y:x+y,i)
            if h > rich:
                rich = h
        return rich
        