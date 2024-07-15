def cal(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    elif op == 3:
        if a < 0 :
            return -(-a // b)
            
        else:
            return a//b
        
    
def dfs(depth, current_value):
    global max_value, min_value
    if depth == N - 1:
        max_value = max(max_value, current_value)
        min_value = min(min_value, current_value)
        return

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            next_value = cal(current_value, numbers[depth+1], i)
            dfs(depth+1, next_value)
            operator[i] += 1
            
N = int(input())
numbers = list(map(int,input().split()))
operator = list(map(int, input().split()))


# max_value = -1e9
# min_value = 1e9
max_value = -float('inf') #가능한 가장 작은값으로 초기화
min_value = float('inf') #가능한 가장 큰 값으로 초기화


dfs(0, numbers[0])



print(max_value)
print(min_value)