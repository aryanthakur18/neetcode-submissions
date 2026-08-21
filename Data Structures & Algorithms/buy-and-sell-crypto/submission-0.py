class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_price=prices[0]
        profit=0
        for i in range(n):
            curr_prof=prices[i]-min_price
            if curr_prof>profit:
                profit=curr_prof
            min_price=min(min_price,prices[i])
        return profit