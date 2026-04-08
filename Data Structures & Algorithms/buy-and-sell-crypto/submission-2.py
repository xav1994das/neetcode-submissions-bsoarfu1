class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        n=len(prices)
        l=0
        r=1
        for r in range (1,n):
            if prices[r]<prices[l]:
                l=r
            else:
                p=max(p, prices[r]-prices[l])
        return p