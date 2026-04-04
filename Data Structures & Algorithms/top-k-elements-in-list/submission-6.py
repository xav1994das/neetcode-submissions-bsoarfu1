from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        hash=defaultdict(int)
        for i in nums:
            hash[i] += 1
        arr=defaultdict(list)
        for key,v in hash.items():
            arr[v].append(key)
        print(arr)
        for i in range(n,0,-1):
            l1=arr[i]
            for ind in range(len(l1)):
                res.append(l1[ind])
                k=k-1
                if k==0:
                    return res
    
        return res


