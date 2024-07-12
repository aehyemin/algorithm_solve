a = []
for i in range(9):
    a.append(int(input()))

b = sorted(a)
print(b[8])

for i in range(9):
    if b[8] == a[i]:
        print(i+1)