n, k = map(int, input().split())
#n가지 종류의 동전, 목표 k원
coin = []
for _ in range(n):
    coin.append(int(input()))
print(n, k)
print(coin)
cnt = 0
for i in range(len(coin)):
    if k % coin[n] == 0:
        cnt += 1
    if k > coin[i]
    
#보류