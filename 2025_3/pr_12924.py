def solution(n):
    ans = 0
    #연속된 자연수들로 표현
    for i in range(1,n+1):
        total = 0
        for num in range(i, n+1):
            total += num
            if total == n:
                ans += 1
                break
            elif total > n:
                break
    return ans
        
