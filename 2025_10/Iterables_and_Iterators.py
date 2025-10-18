from itertools import combinations
n = int(input())
al = list(map(str, input().split()))
k = int(input())
com = []
score = 0
for i in combinations(al, k):
    com.append(i)

for j in range(len(com)):
    if 'a' in com[j]:
        score += 1

print(score / len(com))

