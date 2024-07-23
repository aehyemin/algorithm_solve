import sys 
input = sys.stdin.readline
A = int(input())

sequence = list(map(int, input().split()))
dp = [1]* A
# print(subse)
# print(sequence)

for i in range(1, A):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
    
    
    

