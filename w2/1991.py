

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
# tree = BinarySearchTree()
# tree.root = None

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())

tree = {}
for _ in range(N):
    root, left, right = map(str,input().split())
    tree[root] = (left, right)

# class Node():
#     def __init__(self, item):
#         self.item = item
#         self.left = None
#         self.right = None

#노드 삽입
# 파이썬으로 트리 구현하려면 dictionary 사용 root:key, left,right:value


# 전위 순회 : 노드 방문 -> 왼쪽 서브트리 -> 오른쪽 서브트리
def preorder(n):
    if n != '.': 
        print(n,end='') # 노드 방문
        preorder(tree[n][0]) # 왼쪽 서브 트리 순회
        preorder(tree[n][1]) # 오른쪽 서브 트리 순회


# 중위 순회 : 왼쪽 방문 -> 노드 방문 -> 오른쪽 방문
def inorder(n):
    if n != '.':
        inorder(tree[n][0])    
        print(n,end='') # 노드 방문
        inorder(tree[n][1])
# 후위 순회 : 왼쪽 방문 -> 오른쪽 방문 -> 노드 방문
def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n,end='')


# for item in inputs:
#     tree[item] = Node(item)

preorder('A')
print("")
inorder("A")
print("")
postorder("A")
print("")