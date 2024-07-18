#세로 크기N, 가로 크기M
N, M = map(int, input().split())
node = []
for _ in range(N):
    node.append(input())
# visited = [] * (N+1)




# graph[node] : node와 연결된 node의 리스트 라고 가정할때
def find_tile(N, M, node): #세로 크기N, 가로 크기M
    row_tile = 0 # 열 -
    columm_tile = 0 # 행 |
    
    for i in range(N):
        j = 0
        while j < M:
            if node[i][j] == '-':
                row_tile += 1
                while j < M and node[i][j] == '-':
                    j += 1           
            else :
                j += 1
                

    for j in range(M):
        i = 0
        while i < N:
            if node[i][j] == '|':
                columm_tile += 1
                while i < N and node[i][j] == "|":
                    i += 1
            else:
                i += 1
                
    return row_tile + columm_tile
    
print(find_tile(N, M, node))  
    
