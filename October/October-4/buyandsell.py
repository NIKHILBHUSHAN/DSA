class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        for todayprice in prices:
            if todayprice<minprice:
                minprice=todayprice
            profit=todayprice-minprice
            if profit>maxprofit:
                maxprofit=profit
        return maxprofit