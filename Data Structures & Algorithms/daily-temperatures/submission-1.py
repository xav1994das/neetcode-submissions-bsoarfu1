class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        n=len(temperatures)
        for i in range(n):
            count=0
            j=i+1
            while j<n: 
                if temperatures[i]<temperatures[j]:
                    count+=1
                    res.append(count)
                    break
                else:
                    count+=1
                j+=1
            print(j)
            if j==len(temperatures):
                res.append(0)
        return res