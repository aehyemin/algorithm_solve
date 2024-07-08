
# ans = 0 #놓을 수 있는 방법 수
# 절댓값 계산 abs

def check(n):
    for i in range(n):
        if (here[n] == here[i]) or (n-i == abs(here[i]-here[n])):
            return False
    return True

#######################################################################

def set(depth):
    global result

    if depth == N :
        result += 1 
        return 
    
    for i in range(N):
            # if visited[N]:
            #      continue

        if visited[i] == False :
            here[depth] = i
            
            if check(depth):
                visited[i] = True
                set(depth + 1)
                visited[i] = False
            
#######################################################################

if __name__ == "__main__":
    N = int(input())
    here = [0] * N # 1차원 리스트 적재
    visited = [False] * N # 퀸이 있으면 True
    result = 0

    set(0)
    print(result)
