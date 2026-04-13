class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map=collections.defaultdict(int)
        t_map=collections.defaultdict(int)
        tlen=len(t)
        res=""
        for r in range(tlen):
            t_map[t[r]]+=1

        count=0
        r=0
        l=0
        
        minlen=2**31
        for r in range(len(s)):
            if s[r] in t_map:
                s_map[s[r]]=t_map[s[r]]
            else:
                s_map[s[r]]=0
        
        for r in range(0,len(s)):
            s_map[s[r]]-=1
            if s_map[s[r]]>=0:
                count+=1

            while count==tlen:
                #valid sub
                if r-l+1<minlen:
                    res=s[l:r+1]
                    minlen=r-l+1
                print(res)
                s_map[s[l]]+=1
                if s_map[s[l]]>0:
                    count-=1
                l+=1
        return res