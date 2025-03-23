from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        visited = [[False] * n for i in range(m)]

        def bfs(x,y):
            q.append((x,y))
            visited[x][y] = True

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny] == "1":
                        q.append((nx,ny))
                        visited[nx][ny] = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    cnt += 1

        return cnt
       