import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

# 2 3 2 k마리, p증가율, n총시간
#1초당 p배씩 증가
# 2 * 3 = 6 => 6 * 3 = 18
for i in range(n):
    k = k*p % 1000000007
print(k % 1000000007)
#2마리가 1초당 3배씩 증가 2 * 3 * 3