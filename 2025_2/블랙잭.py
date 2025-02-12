from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))


l=0
r=len(card)
max_cnt = 0
for i in combinations(card, 3):
    cnt = sum(i)
    if max_cnt < cnt <= m:
        max_cnt = cnt
print(max_cnt)
    
        