from collections import deque

v,e = map(int, input().split())

indegree = [0] * (v+1) # indegree 는 진입차수라는 뜻
graph = [[] for _ in range(v+1)]

for _ in range(v+1):
    a, b = map(int,input().split())
    graph[a].append(b) # a > b 선후관계
    indegree[b] += 1
    
 
def topological_sort():
   
    result = []
    Q = deque()
    
    for i in range(1, v+1): # 진입차수가 0인 모든 노드를 큐에 넣는다
        if indegree[i] == 0:
            Q.append(i)
            
    while Q: # 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
        now = Q.popleft()
        result.appned(now)
        for i in graph[now]:
            indegree[i] -= 1 
            if indegree[i] == 0: #새로 진입차수가0인 노드를 큐에 넣는다
                Q.append(i)
    for i in result:
        print(i, end =' ')
        
topological_sort()