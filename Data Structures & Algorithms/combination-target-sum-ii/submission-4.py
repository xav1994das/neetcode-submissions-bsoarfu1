class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        subset=[]
        candidates.sort()
        def func(index,target):
            if target==0:
                res.append(subset[:])
                return

            for i in range(index,n):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                subset.append(candidates[i])
                func(i+1,target-candidates[i])
                subset.pop()
  
        
        func(0,target)
        return res