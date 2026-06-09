class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 100
        for i in range(1,len(prices)):
            sell = prices[i]
            if buy > prices[i-1]:
                buy = prices[i-1]
            if (sell - buy) > res:
                res = sell - buy
        return res