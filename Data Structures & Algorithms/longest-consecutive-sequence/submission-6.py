class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        set1=set()
        maxLen=1
        for i in nums:
            set1.add(i)

        for x in set1:
            ct=0
            p=x
            if p-1 in set1:
                continue
            else:
                #x-1 is not in set 1 
                # this can be a starting point
                while p in set1:
                    p += 1
                    ct += 1
                    maxLen=max(maxLen,ct)
        return maxLen
