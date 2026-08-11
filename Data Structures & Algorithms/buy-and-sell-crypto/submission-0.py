class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            res = max(prices[i] - min_price, res)
        return res
        