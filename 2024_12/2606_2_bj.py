from collections import deque
c = int(input()) #컴퓨터 수
n = int(input()) #연결된 쌍의 수
graph = [[0] * (c+1) for _ in range(c+1)]
for _ in range(n):
    A, B = map(int, input().split())
    graph[A][B] = graph[B][A] = 1

visited = [0]*(c+1)
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        for i in range(1, c+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    
bfs(1)
#1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수
print(sum(visited) - 1)