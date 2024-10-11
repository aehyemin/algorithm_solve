N = input().split()
A = input().split()
B = input().split()

num1 = set(A) - set(B)
num2 = set(B) - set(A)

print(len(num1)+len(num2))