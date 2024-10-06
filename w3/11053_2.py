A = int(input())
seq = list(map(int, input().split()))
print(seq)
l_seq = []

dp = [1] * A

for i in range(1,A):
    for j in range(i):
        if seq[i] > seq[j]: #부분적으로 증가한다면           
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
            
            