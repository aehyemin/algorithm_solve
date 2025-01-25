import sys

input = sys.stdin.readline
jewels = []
# 배낭의무게w, 귀금속종류n
w, n = map(int, input().split())
#전동톱으로 자를수있다
for i in range(n):
    jewel = list(map(int, input().split()))
    jewels.append(jewel)

    #금속의무게m, 무게당가격p
jewels.sort(key = lambda x: x[1], reverse=True)
money = 0

for m,p in jewels:
    if w>=m:
        money += m*p
        w -= m
    else:
        money += w*p
        break

print(money)
    