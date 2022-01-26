from typing import List

prices = [7, 6, 4, 3, 1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i + 1 <= len(prices) - 1:
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
            i += 1
        return profit


s = Solution()
print(s.maxProfit(prices))
