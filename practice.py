n = int(input()) 
num_list = list(map(int, input().split()))
prime = 0

for i in range(len(num_list)):
    if num_list[i] == 1:
        continue
    for b in range(2, num_list[i]):
        if num_list[i] % b == 0:
            break
    else : 
        prime+=1

print(prime)