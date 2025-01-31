import sys
input = sys.stdin.readline

#난로 반지름의 길이 = 반지름의 길이의 배수

n = int(input())
a = list(map(int, input().split()))

cnt = 0
#리스트 안에서의 약수나 리스트 안의 수 하나를 해야됨

min_a = min(a)

ans = []
mode = [0] * 100

for i in a:
    k=2
    while(i>1):
        if i % k == 0:
            ans.append(k)
            while i % k == 0:
                i //= k
        k+=1
for i in ans:
    mode[i] +=1

#최대 몇집이 사용할 수 있는지?
print(max(mode))