def solution(A):
    #n개의 정수 배열 A가 있다
    #1~n+1의 정수가 있는데 이중에 빈 정수 하나를 찾아라
    # [2, 3, 1, 5] 4가 빠짐 
    len_a = len(A)+1
    sum_all = len_a * (len_a+1) // 2
    return sum_all - sum(A)
