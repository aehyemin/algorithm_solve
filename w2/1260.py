import sys
input = sys.stdin.readline
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
# 다음 M 개의 줄에는 간선이 연결하는 두 정점의 번호, 양방향

#N+1개의 행을 가진 리스트를 생성하며, 각 행은N+1개의 0으로 구성
graph = [[0]*(N+1)for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    graph[A][B] = graph[B][A] = 1
#정점 A-B 간선 추가.1대신 다른값을 사용할수도 있지만 가장 간단
#부울 값보다 메모리 사용 최적화 가능 0 1

# DFS 와 BFS 의 방문 기록을 독립적으로 관리
visited = [0]*(N+1)
visited2 = visited.copy()


def dfs(V):
    visited[V] = 1 # 방문처리
    print(V, end=' ') #줄 바꿈 대신 공백
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] ==0:
            dfs(i)
#if graph[v][i]는 두 정점 v,i 가 연결되어 있음
#[v][i]==1 이면 두 정점 사이에 간선 존재


# 큐에서 정점을 하나 꺼냅니다.
# 해당 정점과 인접한 정점들을 모두 방문하고 큐에 넣습니다.
# 큐에서 다음 정점을 꺼내어 위 과정을 반복합니다.
def bfs(V):
    queue = [V]
    visited2[V] =1
    while queue:
     V = queue.pop(0) # 큐에서 첫번째 요소
     print(V, end = ' ')
     for i in range(N+1):
         if visited2[i] == 0 and graph[V][i] == 1:
             queue.append(i)
             visited2[i] = 1

dfs(V)
print()

bfs(V)
print()

#      1
#     / \
#    2 - 3
#   /   / \
#  4 - 5 - 6