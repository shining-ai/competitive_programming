class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i_price in prices:
            if i_price < min_price:
                min_price = i_price
            if i_price - min_price > max_profit:
                max_profit = i_price - min_price

        return max_profit
