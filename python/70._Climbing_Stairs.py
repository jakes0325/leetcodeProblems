class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo: dict[int,int] ={
            1:1,
            2:2
        }
        def climb(n):
            if n in memo:
                return memo[n]
            else:   
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)