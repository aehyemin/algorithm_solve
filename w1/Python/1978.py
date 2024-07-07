n = int(input()) 
num_list = list(map(int, input().split()))
prime = 0

for num in num_list:
    if num == 1:
          continue
     
    for i in range(2,num): #2부터 num-1까지 범위에서
            if num % i == 0 :
                 break
    else:
        prime += 1
print(prime)





