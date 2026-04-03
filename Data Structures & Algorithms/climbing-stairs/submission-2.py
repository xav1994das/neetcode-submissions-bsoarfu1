from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        ways= self.climbStairs(n-1)+self.climbStairs(n-2)
        return ways