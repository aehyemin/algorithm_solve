from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

for i in range(1,n+1):
    graph[i].sort()
#스택
def dfs(v):
    
    stack = [v]
    result = []
    while stack:
        x = stack.pop()
        if visited1[x] == 0:
            visited1[x] = 1
            result.append(x)
            for i in reversed(graph[x]):
                if visited1[i] == 0:
                    stack.append(i)
    return result
    
    
    
#큐
def bfs(v):
    queue = deque([v])
    visited2[v] = 1
    result = []
    while queue:
        v = queue.popleft()
        result.append(v)
       
        for i in graph[v]:
            if visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1
              
    return result
        
dfs_ans = dfs(v)
bfs_ans = bfs(v)

print(" ".join(map(str, dfs_ans)))
print(" ".join(map(str, bfs_ans)))
