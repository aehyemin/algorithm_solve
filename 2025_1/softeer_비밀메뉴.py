import sys

input = sys.stdin.readline

m,n,k = map(int,input().split()) 
#m 이 조작법 앞뒤로 다른 버튼 조작이 있어도 비밀메뉴로 인정
#n 사용자의 버튼 조작을 나타냄
#k 자판기의 총 버튼 , 버튼개수
m_lst = list(input().split())
k_lst = list(input().split())

M = "".join(m_lst)
K = "".join(k_lst)

if M in K:
    print("secret")
elif len(M) > len(M):
    print("normal")
else:
    print("normal")
