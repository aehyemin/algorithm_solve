import sys
input = sys.stdin.readline
b= []
for i in range(3):
    b.append(list(map(int, input().split())))

ans = 10000000
row = []
col = []
#중간 값
def gap(list):
    return max(list) - min(list)
    
#세로 값
for i in range(3):
    row = b[i]
    ans = min(ans, gap(row))
    
#가로 값
for j in range(3):
    col = [b[i][j] for i in range(3)]
    ans = min(ans, gap(col))
    
print(ans)
#높이를 꼭 1로 안맞춰도되나?