class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi=-1
        for x in piles:
            maxi=max(maxi,x)
        l=1
        w=maxi
        res=w
        while l<=w:
            x=(l+w)//2 
            s = 0           
            for p in piles:
                s += math.ceil(p/x)
                if s > h:
                    break
            if s<=h:
                res=x
                w=x-1
            else:
                l=x+1
        return res

            