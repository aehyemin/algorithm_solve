# spanning tree 중 가중치의 합이 최소인 minimum spanning tree
#prim
# 최소 스패닝 트리를 찾기 위해 정점 부분집합에 이웃한 거리들을 판단하며 구한다.
# 신장 트리에 붙은 마디 중 가장 minimun 한 값을 선택하면서 만들어감

# 1. 하나의 꼭지점을 선택하여 이웃한 거리를 구한다
# 2. 가장 최소인 이웃한 거리를 구하고, 정점 부분집합에 이웃한 정점을 추가한다.
# 3. 추가한 정점과 이웃한 거리들을 순회하며, 이웃한 거리를 업데이트 한다.
# 4. 2와 3을 반복하며, 정점 부분집합에 모든 정점이 포함되면 리턴한다.

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
V, E = map(int, input().split())
graph = [ [] for _ in range(V+1) ]

# 각 정점의 가중치와 인접 정보를 넣어주는 반복문
for _ in range(E):
    A, B, C = map(int,input().split())
    graph[A].append([B,C])
    graph[B].append([A,C])


def prim(start):
    visit = [0] * (V+1) # 정점 방문 처리
    q = [[0, start]] # 힙구조를 사용하기 위해 가중치를 앞에 둠
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수

    while cnt < V:
        k, v = heappop(q)
        if visit[v]:
            continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 # 방문 안했으면 방문처리
        ans += k
        cnt += 1
        for u, w in graph[v]:
            if not visit[u]:
                heappush(q,[w,u])
    return ans

print(prim(1))