class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        maxVal=1
        ct=1

        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                ct += 1
            else:
                maxVal=max(maxVal,ct)
                ct=1
        maxVal=max(maxVal,ct)
        return maxVal