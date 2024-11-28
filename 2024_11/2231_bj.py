N = int(input())
#분해합은 N과 N을 이루는 각 자리수의 합
for i in range(1, N+1):
    num = sum(map(int, str(i)))
    num_sum = i + num 
    if num_sum == N:
        print(i)
        break
    if i == N :
        print(0)

