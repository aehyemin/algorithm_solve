k = int(input())
#0이 나오면 최근에 쓴 수를 지운다
num = []

for i in range(k):
    new = int(input())
    if new == 0:
        num.pop()
    else:
        num.append(new)
    

print(sum(num))