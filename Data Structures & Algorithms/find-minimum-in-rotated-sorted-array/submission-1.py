import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mini=sys.maxsize
        while l<=r:
            m=(r+l)//2
            if nums[m]<nums[r]:
                mini=min(mini,nums[m])
                r=m-1
            else:
                mini=min(mini,nums[l])
                l=m+1
            
        return mini

