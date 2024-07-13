import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
preorder = []

while True :
    try:
        N = int(input())
        preorder.append(N)
    except:
        break


def postorder(left, right):
    if left > right: # 범위가 잘못되면 종료
        return
    root = preorder[left]
    div = right + 1
    for i in range(left+1, right+1):
        if root < preorder[i]:
            div = i
            break

# for 

    postorder(left+1, div-1)
    postorder(div, right)
    print(root) # 끝까지 오면 노드 출력 시작

postorder(0, len(preorder)- 1)
