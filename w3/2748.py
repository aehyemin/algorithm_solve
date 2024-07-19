fibo = []

for i in range(91):
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1]+fibo[i-2])
        
n = int(input())

print(fibo[n])

# def fibo() -> int:
#     n = int(input())
#     fibo_list = [0, 1]
#     for i in range(2, n+1):
#         value = fibo_list[i-1] + fibo_list[i-2]
#         fibo_list.append(value)
#     print(fibo_list[n])
    
# fibo()

# n = int(input())

# def fibo(n):
#     if n == 0:
#         return 0
    
#     elif n == 1 or n== 2:
#         return 1
    
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# print(fibo(n))
        
