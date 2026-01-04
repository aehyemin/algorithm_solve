from collections import deque

#R: 순서뒤집기, D: 첫번째 수 버리기(비어있는데 사용하면 에러 발생)

T = int(input())

for i in range(T):
    r_cnt = 0
    p = input() #문자열
    n = int(input())
    arr = input().strip()
    err = False
    
    if n == 0:
        q = deque()
    else:
        q = deque(arr[1:-1].split(","))
        
    #R이 짝수일경우 -> 순서 안바꾸고 앞에 버림
    #R이 홀수일경우 -> 뒤를 버리고 마지막에 reverse
    for j in range(len(p)):
        if p[j] == "R":
            r_cnt += 1
        else: #D일때
            if len(q) == 0:
                print("error")
                err = True
                break
            else:
                if r_cnt % 2 == 0: #r카운트가 짝수면
                    q.popleft()
                else:
                    q.pop()
                    
    if err == True:
        continue    
    
    if r_cnt % 2 == 0:
        print("[", ",".join(q), "]", sep="")
    else:
        q.reverse()
        print("[" + ",".join(q) + "]")