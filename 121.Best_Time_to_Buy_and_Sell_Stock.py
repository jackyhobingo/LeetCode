class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = None
        max_profit = 0
        for p in prices:
            if buy == None:
                buy = p
                continue
            max_profit = max(p-buy, max_profit)
            buy = min(p, buy)
        return max_profit
