# 정수 n 개가 주어졌을때, n 개의 합을 구하는 함수 작성
#def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
# (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)


def solve(a: list) -> int:
    ans = 0
    for i in a:
        ans += a[i]
    return ans

