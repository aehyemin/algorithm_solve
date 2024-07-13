import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

# 방문 여부, 각 인덱스를 노드로 사용해 방문했으면 0을 지우고, 부모 노드를 저장한다.
# 부모 노드를 저장할 배열 초기화, 방문 여부도 확인 가능
parent = [0] * (N+1)
visited = [0] * (N+1)

graph = [ [] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split()) # 연결된 두 정점
    graph[a].append(b)
    graph[b].append(a)


def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0: # 부모 노드가 저장되지 않은 경우
            parent[i] = n
            dfs(i)

dfs(1)

for j in range(2,N+1):
    print(parent[j])