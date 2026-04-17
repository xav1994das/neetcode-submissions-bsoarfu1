class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m=collections.defaultdict(int)

        for i in range(len(nums)):
            m[nums[i]]+=1
            if m[nums[i]]>1:
                return nums[i]
            
            print(m[nums[i]])
        return -1