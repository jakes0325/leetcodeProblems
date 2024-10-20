class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fibonacci(n):
            if n <= 1 and n >= 0:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)


        return fibonacci(n)