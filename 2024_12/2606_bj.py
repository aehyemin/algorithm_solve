c = int(input())
n = int(input())
graph =[[0] * (c+1)for _ in range(c+1)]
for _ in range(n):
    A, B = map(int, input().split())
    graph[A][B] = graph[B][A] = 1
visited = [0] * (c+1)

def dfs(v):
    cnt = 0
    visited[v] = 1
    for i in range(1, c+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)
            cnt += 1
    return cnt

dfs(1)
print(sum(visited) -1)