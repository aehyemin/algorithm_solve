from itertools import combinations
n =  int(input())

s = list(map(int, input().split()))
s.sort()
a = 0


for i in s:
    if a + 1 < i:
        break
    a += i
print(a+1)

