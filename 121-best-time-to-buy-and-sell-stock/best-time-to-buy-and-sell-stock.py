class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if min_price > i:
                min_price = i
            if i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit

        