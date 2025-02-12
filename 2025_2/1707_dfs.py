import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
k = int(input())

def dfs(node):
    if visited[node] == 0:
        visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = -visited[node]
            if not dfs(i):
                return False
        else:
            if visited[i] == visited[node]:
                return False
               
    return True

for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    visited = [0] * (v+1)
    check = True
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    for i in range(1, v+1):
        if visited[i] == 0:
            if dfs(i) == False:
                check = False
    print("YES" if check==True else "NO")
            
    