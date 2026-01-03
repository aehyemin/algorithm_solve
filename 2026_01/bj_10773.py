k = int(input())

arr = []
for i in range(k):
    cur = int(input())
    if cur == 0:
        arr.pop()
    else:
        arr.append(cur)
    
print(sum(arr))