class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = collections.defaultdict(int)
        map1 = collections.defaultdict(int)

        for i in range(len(s1)):
            count[s1[i]]+=1

        n=len(s2)
        r=len(s1)
        l=0
        if n<r:
            return n>r
        for i in range(0,r):
            map1[s2[i]]+=1 
        if count==map1:
            return True
        print(count)
        while r<n:
            map1[s2[r]] += 1 
            r+=1
            map1[s2[l]] -= 1
            if map1[s2[l]]==0:
                map1.pop(s2[l])
            l+=1
            print(map1)
            if count==map1:
                return True
        return False