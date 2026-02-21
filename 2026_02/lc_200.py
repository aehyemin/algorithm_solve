from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #0이 물, 1이땅
        #연결된 땅의 개수, 
        #BFS돌린 함수를 만든 후, for문으로 순회해서 개수 세기
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        q = deque()

        cnt = 0
        def bfs(i,j):
            visited[i][j] = 1
            q.append((i,j))

            while q:
                dx = [1,-1,0,0]
                dy = [0,0,1,-1]
                x,y = q.popleft()
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0<=nx<m and 0<=ny<n and visited[nx][ny] == 0:
                        if grid[nx][ny] == "1":
                            q.append((nx,ny))
                            visited[nx][ny] = 1

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    bfs(i,j)
                    cnt += 1
        return cnt
        
