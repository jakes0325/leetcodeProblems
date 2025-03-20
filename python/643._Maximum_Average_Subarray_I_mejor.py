# tuve que mirar las soluciones
# en esta solucion uso "Sliding window" para poder resolver en O(n)
#
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        L,R = 0,k
        n = len(nums)
        main_sum = curr_sum = sum(nums[L:R])
        while R<n:
            curr_sum += (nums[R]- nums[L])
            main_sum = max(main_sum,curr_sum)
            L += 1
            R += 1
        return (main_sum/k)