class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        n=len(nums)
        nums.sort()
        subset=[]
        def func(index):
            if index==n:
                res.add(tuple(subset))
                return 
            subset.append(nums[index])
            func(index+1)
            subset.pop()
            func(index+1)


        func(0)
        print([list(i) for i in res])
        return ([list(i) for i in res])