def solution(X, Y, D):
    #X to Y보다 크거나 같은 위치로 감, D만큼 점프함
    #Y로 갈 수 있는 최소한의 횟수
    
    #Y-X) // D 면? 75 // 30 = 2 +1 
    jmp = (Y-X) // D + 1
    if (Y-X) % D != 0:
        return jmp
    else:
        return jmp -1
