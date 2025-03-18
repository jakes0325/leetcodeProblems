#print(6&1)
#este mire las soluciones y aprendi de DP (Dinamic Programming)
# -----------------------------------------------------------------------------------------------------------
# The & operator performs a bitwise AND operation between two numbers.
# It compares the binary representation of the numbers bit by bit 
# and returns a new number whose bits are set to 1 only if both corresponding bits in the operands are 1. 
def maxScore(self, A: list[int], x: int) -> int:
        dp = [-x, -x]
        dp[A[0] & 1] = A[0]
        for i in range(1, len(A)):
            dp[A[i] & 1] = max(dp[A[i] & 1], dp[A[i] & 1 ^ 1] - x) + A[i]
        return max(dp)