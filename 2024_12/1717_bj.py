#집합을 합침
def union(b, c):
    b = find(b)
    c = find(c)
    if b < c:
        parent[b] = c
    else:
        parent[c] = b
    

#집합이 포함되었는지 확인
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


n, m = map(int, input().split())
parent = list(range(n+1))

cal = []
for _ in range(m):
    cal.append(map(int, input().split()))
    
for a, b, c in cal:
    if a == 0:
        union(b, c)
    if a == 1:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
    
    

    
    