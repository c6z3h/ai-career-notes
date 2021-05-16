class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.calculate(prices, 0)
    
    
    def calculate(prices, s):
        for x in prices:
            if (s >= len(prices)):
                return 0;
        max = 0
        for s in range(0, len(prices)):             # s = start
            self.maxprofit = 0;
            for i in range(s+1, len(prices)):
                if prices[start] < prices[i]:
                    profit = calculate(prices, i+1) + prices[i] - prices[s];
                    self.maxprofit = profit;
            if self.maxprofit > max:
                max = self.maxprofit;
        return max;
        #sum = 0;
        #for c in (1, 10^4):
	    #    if ((prices[c] > prices[c-1]) and (prices[c] - prices[c-1] >1)):
		#    sum += prices[c] - prices[c-1];
		#    c = c+1;
