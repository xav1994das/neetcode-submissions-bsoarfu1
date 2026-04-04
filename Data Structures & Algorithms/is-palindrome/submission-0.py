class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        h=len(s)-1
        while l<=h:
            if not ('a'<=s[l]<='z' or '0'<=s[l]<='9'):
                l += 1
                continue
            if not ('a'<=s[h]<='z' or '0'<=s[h]<='9'):
                h -= 1
                continue    
            if s[l]!=s[h]:
                return False
            l=l+1
            h=h-1
        return True