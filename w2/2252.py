from collections import deque
#N은 학생의 번호개수, M은 키를 비교한 횟수
N, M = map(int, input().split())
    
indegree = [0] * (N+1) # 진입차수
graph = [[] for i in range(N+1)] # 선후관계


# M개의 줄에 키를 비교한 두 학생의 번호 A,B
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # A > B 선후관계
    indegree[B] += 1
    
def topology_sort():
    result = []
    Q = deque()
    
    for i in range(1,N+1):
        if indegree[i] == 0:
            Q.append(i)
            
    while Q:
        now = Q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)
    for i in result:
        print(i, end = ' ')
    
    
topology_sort()
    
    
