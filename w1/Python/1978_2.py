# 소수 찾기
N = int(input())
prime = 0
num_list = list(map(int,input().split()))

for num in num_list:
    if num == 1:
        continue
        
    for j in range(2,num):
        if num % j == 0:
            break
    else :
        prime+=1
print(prime)