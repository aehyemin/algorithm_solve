def solution(n):
    str_n = str(n)
    ans = list(map(int, reversed(str_n)))
    return ans
