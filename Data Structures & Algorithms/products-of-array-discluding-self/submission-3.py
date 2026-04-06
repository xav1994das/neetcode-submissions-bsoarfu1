class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        op =[1]*n

        op[0]=1
        for i in range(1,n):
            op[i]=nums[i-1]*op[i-1]
        post=1
        for i in range(n-1,-1,-1):
            op[i]=post*op[i]
            post=post*nums[i]
        
        return op

