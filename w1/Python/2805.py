import sys
# 첫째줄 : N = 나무의 수, M = 필요한 나무 길이 
# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
# trees = [20 15 10 17]
# 둘째줄 : H = 나무의 높이 >= M
# 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.



while start <= end:
    count = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            count += tree - mid

    if count >= M:
        start = mid + 1

    else:
        end = mid - 1
print(end)















# print(Tree)




# for i in range(N):
#     allTree = 0
#     allTree += Tree[i]
# allTree

# if allTree - N*H == M:
#     H

# print(H)