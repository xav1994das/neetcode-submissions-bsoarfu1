class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen={}
        s=s.lower()
        t=t.lower()
        for i in s:
            seen[i]=seen.get(i,0)+1
        for i in t:
            if i in seen:
                seen[i]=seen[i]-1
        for ch, count in seen.items():
            if count!=0:
                return False
        return True
        
        
