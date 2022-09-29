class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        graph = 0
        for price in range(len(prices) - 1):
            if prices[price] < prices[price + 1]:
                graph += prices[price + 1] - prices[price]
        return graph
            