# N = int(input())

# fibo = [0] * 100_000_1
# fibo[1] = 1
# fibo[2] = 2
# for i in range(3,N+1):
#     fibo[i] = (fibo[i-1] + fibo[i-2])%15746

# print(fibo[N])
        
    
N = int(input())

fibo = [1, 2]
for i in range(2, N+1):
    fibo.append((fibo[i-1] + fibo[i-2])%15746)
print(fibo[N-1])