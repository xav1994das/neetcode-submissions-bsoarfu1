class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        subset=[]
        def func(index):
            res.append(subset[:])
            for i in range(index,n):
                if i>index and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                func(i+1)
                subset.pop()

            


        func(0)
        print([list(i) for i in res])
        return ([list(i) for i in res])