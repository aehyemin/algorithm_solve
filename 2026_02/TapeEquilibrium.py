def solution(A):
    sum_a = sum(A)
    tmp = A[0]
    result = []
    for i in range(1, len(A)):
        cur = abs(sum_a - 2*tmp)
        tmp += A[i]
        result.append(cur)
    return min(result)
