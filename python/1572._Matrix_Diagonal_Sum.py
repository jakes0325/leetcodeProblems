class Solution:
    def diagonalSum(mat: list[list[int]]) -> int:
        # mat = [[1,2,3],
        #        [4,5,6],
        #        [7,8,9]]
        sum:int = 0
        for row_index, row in enumerate(mat):
            for col_index, value in enumerate(row):
                if row_index == col_index:
                    sum += value
                    continue
                if row_index + col_index == len(row) - 1:
                    sum += value
        return sum
    print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))

