class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j=j+1
                elif sum>0:
                    k=k-1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j=j+1
                    k=k-1

                    while j<=k and nums[j]==nums[j-1]:
                        j=j+1
                    while k>=j and nums[k]==nums[k+1]:
                        k=k-1
                    
        return res
