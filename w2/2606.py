import sys
input = sys.stdin.readline

#첫째줄 N는 컴퓨터의 수, 정점
# M 둘째줄에는 연결된컴퓨터 쌍의 수, 간선
N = int(input())

M = int(input())
graph = [[0]*(N+1)for _ in range(N+1)]

for _ in range(M):
    A,B = map(int, input().split())
    graph[A][B] = graph[B][A] = 1

visited = [0] * (N+1)

def dfs(V):
    cnt = 0
    visited[V] = 1
    # print(V, end= ' ')
    for i in range(1,N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)
            cnt += 1
    return cnt

            
        
dfs(1)
print(sum(visited)-1)



