class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26
        count2=[0]*26

        n1=len(s1)
        n2=len(s2)

        if n1>n2:
            return False
        
        for i in range(0,n1):
            count1[ord(s1[i])-97]+=1
            count2[ord(s2[i])-97]+=1
        matches=0

        for i in range(0,26):
            if count1[i]==count2[i]:
                matches+=1
        if matches==26:
            return True
        l=0
        r=n1
        while r<n2:
            index=ord(s2[l])-97
            if count2[index]==count1[index]:
                matches-=1
            count2[index]-=1
            if count2[index]==count1[index]:
                matches+=1
            l=l+1


            index=ord(s2[r])-97
            if count2[index]==count1[index]:
                matches-=1
            count2[index]+=1
            if count2[index]==count1[index]:
                matches+=1
            r=r+1

            if matches==26:
                return True
        return False
