# 최소 스패닝 트리를 찾기 위해 정점 부분집합에 이웃한 거리들을 판단하며 구한다.
# 신장 트리에 붙은 마디 중 가장 minimun 한 값을 선택하면서 만들어감

# 1. 하나의 꼭지점을 선택하여 이웃한 거리를 구한다
# 2. 가장 최소인 이웃한 거리를 구하고, 정점 부분집합에 이웃한 정점을 추가한다.
# 3. 추가한 정점과 이웃한 거리들을 순회하며, 이웃한 거리를 업데이트 한다.
# 4. 2와 3을 반복하며, 정점 부분집합에 모든 정점이 포함되면 리턴한다.

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
input = sys.stdin.readline

#inf 양의 무한대. float 에만 무한수가 적용가능하다
#첫째줄에 정점의 개수 V, 간선의 개수 E 가 주어진다.
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 ABC가 주어짐
# A번 정점과 B정점이 가중치 C인 간선으로 연결되어있다.(C는 음수일수도있다.)
V, E = map(int,input().split())
G = [[float('inf')] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int,input().split())
    G[a][b] = c
    G[b][a] = c
for i in range(V):
    G[i][i] = 0

pprint(G)

def Prim(G, source):
    answer = []
    dist = [G[source][i] for i in range(V)]
    nearest = [0] * V

    while len(answer) < V:
        minValue = float('inf')
        vnear = 0

        #find minValue
        for i in range(V):
            if 0 < dist[i] < minValue:
                minValue = dist[i]
                vnear = i
        if minValue == float('inf') and vnear ==0:
            break
            
        answer.append((vnear,minValue))
        dist[vnear] = -1

        for i in range(1,V):
            if G[i][vnear] < dist[i]:
                dist[i] = G[i][vnear]
                nearest[i] = vnear
    return answer
print(Prim(G,0))








