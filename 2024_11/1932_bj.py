n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
    
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택

ans = 0
for i in range(1,n):
    for j in range(len(triangle[i])):
        if j==0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(max(triangle[-1]))
