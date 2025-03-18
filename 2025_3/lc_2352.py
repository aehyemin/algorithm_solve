class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i] == [grid[k][j] for k in range(len(grid))]:
                    count += 1
        return count