# find the best buy and sell time
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = len(prices)-1
        stock = 0
        sell = []
        buy = []
        while i>0:
            if prices[i]>prices[i-1] and stock==0:
                sell.append(i)
                stock = 1
            elif prices[i]<prices[i-1] and stock==1:
                buy.append(i)
                stock = 0
            i-=1
        if stock==1:
            if prices[0]<prices[sell[-1]]:
                buy.append(i)
            else:
                sell = sell[:-1]
        profit = 0
        if len(sell)!=len(buy):
            return 'ERROR!'
        for i in range(len(sell)):
            profit += prices[sell[i]]-prices[buy[i]]
        
        return profit

# find the max profit only
    # runtime: O(n)
    # memory: O(1)
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit