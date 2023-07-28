#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 4 min
# optimal (beat 99% and 81%)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float("inf")
        profit = 0
        for p in prices:
            low = min(p, low)
            profit = max(profit, p - low)
        
        return profit

