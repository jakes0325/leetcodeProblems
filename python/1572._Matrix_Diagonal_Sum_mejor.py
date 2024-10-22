class Solution:
    def diagonalSum(mat: list[list[int]]) -> int:
        # mat = [[1,2,3],
        #        [4,5,6],
        #        [7,8,9]]
        sum:int = 0
        l:int = len(mat) 
        for i in range(l):
            sum += mat[i][i]
            sum += mat[l-1-i][i]
        if l % 2 != 0:
            sum -= mat[l//2][l//2]
        return sum
    print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))