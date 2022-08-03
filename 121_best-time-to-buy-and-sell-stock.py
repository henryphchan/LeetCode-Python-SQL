# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        profit = 0
        maxProfit = 0
        for d in range(1,len(prices)):
            if prices[d] < prices[buyDay]:
                buyDay = d
            if prices[d] > prices[buyDay]:
                profit = prices[d] - prices[buyDay]
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([4,999,1,2,3]))
    print(s.maxProfit([1,1,1,1]))
    print(s.maxProfit([999,1,2,3]))