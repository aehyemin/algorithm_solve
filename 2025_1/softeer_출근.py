import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]for i in range(n+1)]
graph_r = [[]for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y) #간선으로 나가는
    graph_r[y].append(x) #간선으로 들어오
s, t = map(int,input().split())

# print(n, m)
# print(graph)
# print(graph_r)
# print(s,t)

def dfs(now, graph, visit):
    if visit[now] == 1:
        return
    visit[now] = 1
    for neighbor in graph[now]:
        dfs(neighbor, graph, visit)
    return
fromS = [0] *(n+1)
fromS[t] = 1
dfs(s, graph, fromS)

fromT = [0] * (n+1)
fromT[s] = 1
dfs(t, graph, fromT)

toS = [0] * (n+1)
dfs(s, graph_r, toS)

toT = [0] * (n+1)
dfs(t, graph_r, toT)

cnt = 0
for i in range(1, n+1): #0안씀
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt+=1
print(cnt-2)