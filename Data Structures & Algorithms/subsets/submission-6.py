class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        temp=[]
        def f(index):
            if index==n:
                res.append(temp[:])
                print(temp)
                return
            temp.append(nums[index])
            f(index+1)
            temp.remove(nums[index])
            f(index+1)

        
        f(0)
        return res
            