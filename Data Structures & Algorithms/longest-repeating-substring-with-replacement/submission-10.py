class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        count=collections.defaultdict(int)
        maxFreq=0
        L=0
        res=0
        for i  in range(len(s)):
            ch=s[i]
            count[ch]+= 1
            maxFreq=max(maxFreq,count[ch])
            R=i
            if R-L+1 - maxFreq<=k:
                res=max(res,R-L+1)
            else:
                count[s[L]]-=1   
                L=L+1
                
            
        return res