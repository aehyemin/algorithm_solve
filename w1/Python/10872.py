# n = int(input())

# def factorial(n:int) -> int :
#     if n == 0 :
#         return 1 
#     else :  
#         return n * factorial(n-1)

# print(factorial(n))

n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)

