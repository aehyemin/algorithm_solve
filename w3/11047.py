N, K = map(int, input().split())
price = []
for _ in range(N):
    price.append(int(input()))
    
count = 0   

for i in range(N-1,-1,-1):

    if K >= price[i]:
        count += K // price[i]
        K = K % price[i]

print(count)

    