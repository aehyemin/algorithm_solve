'''
문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
'''

'''
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
런타임 에러 발생
'''

'''
a,b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
pritn(a/b)가 정수가 아니고 2.33333333335 이렇게 float 로 소수점이 출력됨 정수 처리를 해줘야 할듯
'''

'''
변수가 많아지면 
a,b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)
sys.stdin.readline()
'''

a,b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)


