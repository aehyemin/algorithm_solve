# 최소 스패닝 트리를 찾기 위한 탐욕 알고리즘. 
# 각 마디 마다 자신만 포함하는 V의 서로소 부분 집합을 만드는 걸로 시작하여,
#  가중치가 작은 간선을 검사하여 생성하는 알고리즘

# 1. 이음선을 가중치가 작은것부터 차례로 정렬한다
# 2. 사이클이 형성되지 않는 가중치가 가장 작은 간선을 선택한다.
# 3. 총 V-1개의 간선이 선택될 때가지 반복한다.

# 사이클이 형성되었는지 아닌지 찾기 위해 분리집합 사용.
# 간선이 스패닝 트리에 추가될 때마다 Parent 관계를 만들어서 
# 두 정점이 같은 최상위 Parent를 갖는다면 사이클이 발생함을 의미한다.
# 사이클이 발생하지 않는 경우에는 서로의 최상위 parent를 연결한다.
#또한, 작은 가중치의 이음선을 찾기 위해 최소 힙을 이용한다.

def pprint(arr):
    for line in arr:
        print(line)
# 5 7
# 0 1 1
# 0 2 3
# 1 2 3
# 1 3 6
# 2 3 4
# 2 4 2
# 3 4 5
import sys
import heapq as hq

V, E = map(int, sys.stdin.readline().split(" "))

W = [[float('inf')] * V for _ in range(V)]
global parent
parent = [i for i in range(V)]

h = []

for _ in range(E):
    i, j, w = map(int, sys.stdin.readline().split(" "))
    hq.heappush(h, (w, i, j))
print(h)

def findRoot(x):
    if parent[x] == x:
        parent[x] = findRoot(parent[x])
        return parent[x]
    
def union(u,v):
    root1 = findRoot(u)
    root2 = findRoot(v)
    parent[root2] = root1

def Kruskal(heap):
    answer = []
    while len(answer) <(V-1) and heap:
        w,i,j = hq.heappop(heap)
        print(w,i,j)

        if findRoot(i) == findRoot(j):
            continue
        union(i,j)
        answer.append((i,j,w))
        
        print(parent)

    return answer
print(Kruskal(h))