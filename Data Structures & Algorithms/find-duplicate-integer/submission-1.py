class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        #the slow and the fast intersect each other
        #now find the entry cycle to the loop

        slow2=0
        while True:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow==slow2:
                return slow
