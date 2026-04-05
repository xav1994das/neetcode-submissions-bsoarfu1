class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod=1
        ct=0
        output=[0 for _ in range(n)]
        for i in range (n):
            if nums[i]!=0:
                prod *= nums[i]
            else:
                ct+=1

        if ct>1:
            return output
        print(prod)
        for i in range (0,n):
            if nums[i]==0:
                output[i]=prod
            else:
                if ct>0:
                    output[i]=0
                else:
                    output[i]=prod//nums[i]

        return output