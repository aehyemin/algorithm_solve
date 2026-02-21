def solution(X, A):
    #개구리는 0에 있음, 근데 x+1로 가고싶음
    #배열 A가 주어짐. K초에 나뭇잎이 떨어짐
    #한번에 한개만 건널 수 있음. 즉, 1 .. X 까지 나뭇잎이 전부 있어야함
    #조건을 만족하는 가장 빠른 초 
    #X가 5면 len(set) = 5면?

    seen = set()
    for i in range(len(A)):
        if A[i] in seen:
            continue
        else:
            if A[i] <= X:
                seen.add(A[i])

        if len(seen) == X:
            return i
    return -1
