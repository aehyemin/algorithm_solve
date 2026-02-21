def solution(A):
    #1 부터 N까지의 순열. 각 숫자는 한번만 등장
    #순열이면 1, 아니면 0 반환
    seen = set()
    for i in range(len(A)):
        if 1 <= A[i] <= len(A) and A[i] not in seen:
            seen.add(A[i])
        else:
            return 0
    if len(seen) == len(A):
        return 1
    return 0
