class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hash = {}
        col_hash = {}
        for row in grid:
            rows = tuple(row)
            row_hash[rows] = row_hash.get(rows, 0) + 1
        for i in range(len(grid)):
            col = [grid[k][i] for k in range(len(grid))]
            cols = tuple(col)
            col_hash[cols] = col_hash.get(cols, 0) + 1

        cnt = 0
        for ans in row_hash:
            if ans in col_hash:
                cnt += row_hash[ans] * col_hash[ans]
        return cnt