class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def f(index,temp):
            nonlocal res,n
            if index==n:
                res.append(temp[:])
                print(temp)
                return
            temp.append(nums[index])
            f(index+1,temp)
            temp.remove(nums[index])
            f(index+1,temp)

        
        f(0,[])
        return res
            