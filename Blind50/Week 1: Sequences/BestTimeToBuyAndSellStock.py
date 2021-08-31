class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Kadane's Algorithm?
        n = len(prices)
        prev_price = prices[0]
        profit = 0
        
        for i in range(1,n):
            price = prices[i]
            
            if price < prev_price:
                prev_price = price
            else:
                profit = max(profit, price - prev_price)
                prev_price = min(prev_price, price)
                
        return profit
