import sys

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
def dfs(a):
    global result
    visited[a] = True
    
    for i in graph[a]:
        if not visited[i]:
            dfs(i)
            result +=1


dfs(1)
print(result)

