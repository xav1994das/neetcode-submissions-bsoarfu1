class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def func(index):
            if index==n:
                res.append([k for k in nums])
                return
            for i in range(index, n):
                nums[index], nums[i]=nums[i], nums[index]
                func(index+1)
                nums[index], nums[i]=nums[i], nums[index]
        
        func(0)
        return res