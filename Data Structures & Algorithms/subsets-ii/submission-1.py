class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        subset=[]
        def func(index):
            if index==n:
                res.append(subset[:])
                return 
            subset.append(nums[index])
            func(index+1)
            subset.pop()
            while index+1<n and nums[index]==nums[index+1]:
                index+=1
            func(index+1)


        func(0)
        print([list(i) for i in res])
        return ([list(i) for i in res])