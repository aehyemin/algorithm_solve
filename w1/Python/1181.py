N = int(input())
num_list = []
for i in range(N):
   num_list.append((input()))

new_list =list(set(num_list))
new_list.sort()
new_list.sort(key=len)

for i in new_list:
    print(i)
