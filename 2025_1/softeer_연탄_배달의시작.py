import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

town = list(map(int, input().split()))


arr = []
for i in combinations(town, 2):
    arr.append(i)

shorts = []

for i in range(len(arr)):
    short = arr[i][1] - arr[i][0]
    shorts.append(short)

way = min(shorts)
cnt = 0
for i in shorts:
    if way == i:
        cnt+=1

print(cnt)
#거리가 가까운 두 마을 먼저 방문함, 처음방문할 가능성이 있는 마을 조합의 수