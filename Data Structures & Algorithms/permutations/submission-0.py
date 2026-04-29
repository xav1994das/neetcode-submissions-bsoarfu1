class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ds=[]
        res=[]

        n=len(nums)
        hmap=collections.defaultdict(int)
        def backtrack():
            if len(ds)==n:
                res.append(ds[:])
                return
            for i in range(n):
                if hmap[nums[i]]==0:
                    ds.append(nums[i])
                    hmap[nums[i]]=1
                    backtrack()
                    hmap[nums[i]]=0
                    ds.pop()
                



        backtrack()
        return res