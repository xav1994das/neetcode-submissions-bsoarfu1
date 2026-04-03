class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=set()
        seen={}
        for i in range(n):
            seen={}
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in seen:
                    res.add(tuple(sorted([third, nums[i],nums[j]])))
                seen[nums[j]]=True
        print(res)
        return [list(i) for i in res]