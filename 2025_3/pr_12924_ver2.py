def solution(n):
    left = 0
    cnt = 0
    total = 0
    for i in range(1, n+1):
        total += i
        while total > n and left < i:
            total -= left
            left += 1
            
        if total == n:
            cnt += 1  
    return cnt
