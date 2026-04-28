class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        n=len(nums)
        def func(index,target):
            if index==n:
                if target==0:
                    res.append(subset[:])
                return
            
            if nums[index]<=target:
                subset.append(nums[index])
                func(index,target-nums[index])
                subset.pop()
            func(index+1, target)        
        func(0,target)
        return res
        