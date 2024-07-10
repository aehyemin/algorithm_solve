import sys
A, B, C = map(int, sys.stdin.readline().split())

# result = A ** B % C
# print(result)

def power_mod(a, b, c):
    if b == 0 :
        return 1
    
    elif b == 1:
        return a % c

    elif b % 2 == 0:
        return (power_mod(a, b//2, c) ** 2) %c
    else: 
        return (power_mod(a, b//2, c) ** 2 )*a %c
print(power_mod(A, B, C))