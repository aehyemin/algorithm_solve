N = int(input())
city = []

visited = [0] * N


for _ in range(N):
    city.append(list(map(int,input().split())))

result = 1e9 # 초기값 설정


def dfs(start:int, cost:int, count:int) -> None:
   global result
   if count == N-1  and city[start][0] != 0:
        result = min(result, cost + city[start][0])
        return
   
   for i in range(N):
       if visited[i] == 0 and city[start][i] != 0:
           visited[i] = 1
           next_cost = cost + city[start][i]
           dfs(i, next_cost, count+1)
           visited [i] = 0

visited[0] = 1               
dfs(0,0,0)
print(result)
