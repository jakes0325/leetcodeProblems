class Solution:
    def minPartitions(self, n: str) -> int:
        max:int
        max = int(n[0])
        for i in range(len(n)):
            if max < int(n[i]):
                max = int(n[i])
        return max
    
if __name__  == "__main__":
    num = Solution.minPartitions(Solution,"27346209830709182346")
    print(f"el maximo es:{num}")