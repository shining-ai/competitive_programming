class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        profit = 0

        for i_price in prices:
            if i_price < buy_price:
                buy_price = i_price
            elif i_price > buy_price:
                profit += i_price - buy_price
                buy_price = i_price

        return profit
