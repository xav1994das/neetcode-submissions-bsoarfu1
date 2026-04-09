from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        seen=defaultdict(int)
        l=r=mx=0
        r=-1
        for i in range (n):
            if s[i] in seen:
                l=max(l,seen[s[i]]+1)
            
            seen[s[i]]=i
            r+=1
            mx=max(mx,r-l+1)

        return mx