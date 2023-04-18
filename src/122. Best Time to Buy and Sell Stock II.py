class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        li = [0] * len(prices)
        for i in range(1, len(prices)):
            li[i] = prices[i] - prices[i - 1]
        profit = 0
        for i in range(len(li)):
            if li[i] > 0:
                profit += li[i]
        return profit