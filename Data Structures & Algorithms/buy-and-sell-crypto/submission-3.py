class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_sell = 0
        profit = 0

        for i in range(len(prices)-1, -1, -1):
            
            price = prices[i]
            if price > best_sell:
                best_sell = price
            else:
                profit = max(profit, best_sell - prices[i])
        return profit




        