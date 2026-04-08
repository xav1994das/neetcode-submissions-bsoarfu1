class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        n=len(prices)
        for i in range (n):
            for j in range (i+1,n):
                if prices[j]>prices[i]:
                    p=max(p, prices[j]-prices[i])

        return p