from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) 
    graph[v].append(u)

ans = 0
#연결 요소는 그래프의 개수 또는 영역의 개수수
visited = [False] * (n+1)
def bfs(a):
    q = deque()
    q.append(a)
    
    visited[a] = 1
    
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        ans += 1
        
print(ans)
    
    
ans = 0
visited = [False] * (n+1)
def dfs(a):
    
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            dfs(i)
            
            
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        ans += 1
        
print(ans)