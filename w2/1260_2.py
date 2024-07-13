import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

for _ in range(M+1):
    A, B = map(int,input().split())


def dfs(graph, start):
    visited = [] 
    stack = [start]
    while stack:
        node.pop()
        if nide not in visited:
            visited.append(node)
            stack.extend(graph[node]- set(visited))
    return visited
    
# 큐는 스택과 다ㅐ르게 먼저 들어온것이 먼저 나가는 선입선출
from collections import deque
def bfs(graph, start):
    visited = []
    queue = deque([start]) # 시작 노드를 큐에 저장
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node] - set(visited)) # 방문하지 않은 인접 노드를 큐에 추가
    return visited